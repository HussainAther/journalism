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
