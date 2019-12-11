# Load required packages.
library(readr)
library(ggplot2)
library(gganimate)
library(scales)
library(dplyr)

# Load data.
nations <- read_csv("data/wcsj/nations.csv")

# Make sure that year is treated as an integer.
nations <- nations %>%
    mutate(year = as.integer(year))

# Filter for 2016 data only.
nations2016 <- nations %>%
  filter(year == 2016)
