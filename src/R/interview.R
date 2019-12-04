library(readr)
library(dplyr)
library(lubridate)
library(DT)

# Looking for leads and context for stories.

# Load ca medical board disciplinary actions data.
ca_discipline <- read_csv("../../data/mbc/ca_discipline.csv")

# View structure of data.
glimpse(ca_discipline)

# Look at types of disciplinary actions.
types <- ca_discipline %>%
  select(action_type) %>%
  unique()

# Make a searchable web table.
datatable(types, extensions = "Responsive")

# Clean data for reprimands.
ca_discipline <- ca_discipline %>%
  mutate(action_type = case_when(grepl("reprimand", ignore.case = TRUE, action_type) ~ "Reprimand",
                                 TRUE ~ action_type))

# Filter for license revocations only.
revoked <- ca_discipline %>%
  filter(action_type == "Revoked")
  
datatable(revoked, extensions = "Responsive")

# Filter for license revocations by doctors based in California, and sort by city.
revoked_ca <- ca_discipline %>%
  filter(action_type == "Revoked"
         & state == "CA") %>%
  arrange(city)

datatable(revoked_ca, extensions = "Responsive")

# Extract year and month from action_date.
ca_discipline <- ca_discipline %>%
  mutate(year = year(action_date),
         month = month(action_date))

# License revokations for doctors based in California, by year.
revoked_ca_year <- ca_discipline %>%
  filter(action_type == "Revoked" 
         & state == "CA") %>%
  group_by(year) %>%
  summarize(revocations = n())

datatable(revoked_ca_year, extensions = "Responsive")

# License revokations for doctors based in California, by month.
revoked_ca_month <- ca_discipline %>%
  filter(action_type == "Revoked" 
         & state == "CA"
         & year >= 2009) %>%
  group_by(month) %>%
  summarize(revocations = n())

datatable(revoked_ca_month)

# License revocations for doctors based in California, by month.
revoked_ca_month <- ca_discipline %>%
  filter(action_type == "Revoked" 
         & state == "CA"
         & year != 2008) %>%
  group_by(month) %>%
  summarize(revocations = n())

# Disciplinary actions for doctors in California by year and month, from 2009 to 2017.
actions_year_month <- ca_discipline %>%
  filter(state == "CA"
         & year >= 2009) %>%
  group_by(year, month) %>%
  summarize(actions = n()) %>%
  arrange(year, month)

datatable(actions_year_month, extensions = "Responsive")

# Load opioid prescription data.
ca_opioids <- read_csv("../../data/mbc/ca_medicare_opioids.csv")

glimpse(ca_opioids)

# Create a summary, showing the number of opioid prescriptions written by each provider, the total cost of the opioids prescribed, and the cost per claim.
provider_summary <- ca_opioids %>% 
  group_by(npi,
           nppes_provider_last_org_name,
           nppes_provider_first_name,
           nppes_provider_city,
           specialty_description) %>%
  summarize(prescriptions = sum(total_claim_count),
            cost = sum(total_drug_cost)) %>%
  mutate(cost_per_prescription = cost/prescriptions) %>%
  arrange(desc(prescriptions))

datatable(provider_summary, extensions = "Responsive")

library(ggplot2)
library(scales)
library(plotly)

# Histogram of the costs data.
ggplot(provider_summary, aes(x = prescriptions)) +
  geom_histogram()

ggplot(provider_summary, aes(x = prescriptions)) +
  geom_histogram(binwidth = 50) +
  theme_minimal() +
  scale_x_continuous(limits = c(0,3000),
                     labels = comma) +
  scale_y_continuous(labels = comma)

median(provider_summary$prescriptions)

# Make a scatterplot of prescriptions and costs data.
scatterplot <- ggplot(provider_summary, aes(x = prescriptions, 
                                            y = cost,
                                            text = paste0("<b>Name: </b>",nppes_provider_first_name," ",nppes_provider_last_org_name,"<br>",
                                                          "<b>Location: </b>",nppes_provider_city,"<br>",
                                                          "<b>Specialty: </b>",specialty_description,"<br>",
                                                          "<b>NPI: </b>",npi))) +
  geom_point(alpha = 0.3) +
  theme_minimal() +
  scale_x_continuous(labels = comma) +
  scale_y_continuous(labels = dollar)

plot(scatterplot)

# Make interactive version with tooltip.
ggplotly(scatterplot, tooltip = "text") %>%
  config(displayModeBar = FALSE)
