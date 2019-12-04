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
