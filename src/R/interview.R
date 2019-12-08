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

# Load data.
npi_license <- read_csv("../../data/mbc/npi_license.csv")

# Join those two data frames.
ca_discipline_npi <- left_join(ca_discipline, npi_license)

# Join those two data frames.
ca_discipline_npi <- left_join(ca_discipline, npi_license, by = "license")

datatable(ca_discipline_npi, extensions = "Responsive")

# Join disciplinary action data to the opioid prescription data.
provider_summary_actions <- inner_join(provider_summary, ca_discipline_npi, by = "npi") %>%
  arrange(desc(prescriptions))

datatable(provider_summary_actions,  extensions = "Responsive")

# change case of variables to be used in the join
ca_discipline_npi <- ca_discipline_npi %>%
  mutate(last_name = toupper(last_name),
         first_name = toupper(first_name),
         city = toupper(city))

# Join disciplinary action data to the opioid prescription data.
provider_summary_actions_2 <- inner_join(provider_summary, ca_discipline_npi, by = c("nppes_provider_last_org_name" = "last_name", 
                                                                                 "nppes_provider_first_name" = "first_name",
                                                                                 "nppes_provider_city" = "city")) %>%
  arrange(desc(prescriptions))

# Join disciplinary action data to the opioid prescription data.
provider_summary_actions_extra <- anti_join(provider_summary_actions_2, provider_summary_actions)

datatable(provider_summary_actions_extra, extensions = "Responsive")


 # doctors in Berkeley or Oakland who have had their licenses revoked 
revoked_oak_berk <- ca_discipline %>%
  filter(action_type == "Revoked"
       & (city == "Oakland" | city == "Berkeley"))

# doctors in Berkeley who had their licenses revoked
revoked_berk <- ca_discipline %>%
  filter(action_type == "Revoked"
       & city == "Berkeley")

# doctors in Oakland who had their licenses revoked
revoked_oak <- ca_discipline %>%
  filter(action_type == "Revoked"
       & city == "Oakland")

# doctors in Berkeley or Oakland who have had their licenses revoked
revoked_oak_berk <- bind_rows(revoked_oak, revoked_berk)

# write data to CSV file
write_csv(revoked_oak_berk, "../../data/mbc/revoked_oak_berk.csv", na = "")

# extract year and month from action_date
ca_discipline <- ca_discipline %>%
  mutate(year = year(action_date),
         month = month(action_date))

# license revokations for doctors based in California, by year
revoked_ca_year <- ca_discipline %>%
  filter(action_type == "Revoked" 
         & state == "CA") %>%
  group_by(year) %>%
  summarize(revocations = n())

 # license revokations for doctors based in California, by month
revoked_ca_month <- ca_discipline %>%
  filter(action_type == "Revoked" 
         & state == "CA"
         & year >= 2009) %>%
  group_by(month) %>%
  summarize(revocations = n())

# license revokations for doctors based in California, by month
revoked_ca_month <- ca_discipline %>%
  filter(action_type == "Revoked" 
         & state == "CA"
         & year != 2008) %>%
  group_by(month) %>%
  summarize(revocations = n())

# disciplinary actions for doctors in California by year and month, from 2009 to 2017
actions_year_month <- ca_discipline %>%
  filter(state == "CA"
         & year >= 2009) %>%
  group_by(year, month) %>%
  summarize(actions = n()) %>%
  arrange(year, month)

# load opioid prescription data
ca_opioids <- read_csv("../../data/mbc/ca_medicare_opioids.csv")

# look at the data
View(ca_opioids)


# Create a summary, showing the number of opioid prescriptions written by each provider, the total cost of the opioids prescribed, and the cost per claim
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

library(ggplot2)
library(scales)

# histogram of the costs data
ggplot(provider_summary, aes(x = prescriptions)) +
  geom_histogram()

ggplot(provider_summary, aes(x = prescriptions)) +
  geom_histogram(binwidth = 50) +
  theme_minimal() +
  scale_x_continuous(limits = c(0,3000),
                     labels = comma) +
  scale_y_continuous(labels = comma)

#### Make a scatterplot of prescriptions and costs data
ggplot(provider_summary, aes(x = prescriptions, y = cost)) +
  geom_point(alpha = 0.3) +
  geom_smooth(method = lm) +
  theme_minimal() +
  scale_x_continuous(labels = comma) +
  scale_y_continuous(labels = dollar)

# load data
npi_license <- read_csv("../../data/mbc/npi_license.csv")

# join those two data frames
ca_discipline_npi <- left_join(ca_discipline, npi_license)
 
# join disciplinary action data to the opioid prescription data
provider_summary_actions <- inner_join(provider_summary, ca_discipline_npi, by = "npi") %>%
  arrange(desc(prescriptions))

# change case of variables to be used in the join
ca_discipline_npi <- ca_discipline_npi %>%
  mutate(last_name = toupper(last_name),
         first_name = toupper(first_name),
         city = toupper(city))

# join disciplinary action data to the opioid prescription data
provider_summary_actions_2 <- inner_join(provider_summary, ca_discipline_npi, by = c("nppes_provider_last_org_name" = "last_name", 
                                                                                     "nppes_provider_first_name" = "first_name",
                                                                                     "nppes_provider_city" = "city")) %>%
  arrange(desc(prescriptions))

# join disciplinary action data to the opioid prescription data
provider_summary_actions_extra <- anti_join(provider_summary_actions_2, provider_summary_actions)






