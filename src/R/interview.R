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
