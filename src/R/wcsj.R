setwd("../..") # Move up to the journalism directory
save.image("data/wcsj/wcsj.RData") # Save data here 
install.packages("tidyverse") # Install tidyverse, if you haven't already
library(readr) # Load required packages
library(dplyr)
library(ggplot2)
pfizer <- read_csv("data/wcsj/pfizer.csv") # Load data of pfizer payments to doctors 
                                 # and warning letters sent by food and drug 
                                 # adminstration
fda <- read_csv("data/wcsj/fda.csv")
str(pfizer) # View structure of data
pfizer$total # Print values for total in pfizer data
pfizer$total <- as.numeric(pfizer$total) # Convert total to numeric variable
str(pfizer)
summary(pfizer) # Summary of pfizer data

# Doctors in California who were paid $10,000 or more by Pfizer to run “Expert-Led Forums.”
ca_expert_10000 <- pfizer %>%
  filter(state == "CA" & total >= 10000 & category == "Expert-Led Forums") %>%
  arrange(desc(total))

# Doctors in California *or* New York who were paid $10,000 or more by Pfizer to run "Expert-Led Forums".
ca_ny_expert_10000 <- pfizer %>%
  filter((state == "CA" | state == "NY") & total >= 10000 & category == "Expert-Led Forums") %>%
  arrange(desc(total))

# Doctors in states *other than* California who were paid $10,000 or more by Pfizer to run "Expert-Led Forums".
not_ca_expert_10000 <- pfizer %>%
  filter(state != "CA" & total >= 10000 & category=="Expert-Led Forums") %>%
  arrange(desc(total))

# 20 doctors across the four largest states (CA, TX, FL, NY) who were paid the most for professional advice.
ca_ny_tx_fl_prof_top20 <- pfizer %>%
  filter((state=="CA" | state == "NY" | state == "TX" | state == "FL") & category == "Professional Advising") %>%
  arrange(desc(total)) %>%
  head(20)

# Filter the data for all payments for running Expert-Led Forums or for Professional Advising, and arrange alphabetically by doctor (last name, then first name).
expert_advice <- pfizer %>%
  filter(category == "Expert-Led Forums" | category == "Professional Advising") %>%
  arrange(last_name, first_name)

# Use pattern matching to filter text.
expert_advice <- pfizer %>%
  filter(grepl("Expert|Professional", category)) %>%
  arrange(last_name, first_name)

not_expert_advice <- pfizer %>%
  filter(!grepl("Expert|Professional", category)) %>%
  arrange(last_name, first_name)

# Merge/append data frames.
pfizer2 <- bind_rows(expert_advice, not_expert_advice)

# Write expert_advice data to a csv file.
write_csv(expert_advice, "data/wcsj/expert_advice.csv", na="")

# Calculate total payments by state.
state_sum <- pfizer %>%
  group_by(state) %>%
  summarize(sum = sum(total)) %>%
  arrange(desc(sum))

# As above, but for each state also calculate the median payment, and the number of payments.
state_summary <- pfizer %>%
  group_by(state) %>%
  summarize(sum = sum(total), median = median(total), count = n()) %>%
  arrange(desc(sum))

# As above, but group by state and category.
state_category_summary <- pfizer %>%
  group_by(state, category) %>%
  summarize(sum = sum(total), median = median(total), count = n()) %>%
  arrange(state, category)

# FDA warning letters sent from the start of 2005 onwards.
post2005 <- fda %>%
  filter(issued >= "2005-01-01") %>%
  arrange(issued)

# Count the letters by year.
letters_year <- fda %>%
  mutate(year = format(issued, "%Y")) %>%
  group_by(year) %>%
  summarize(letters=n())

# Add new columns showing many days and weeks elapsed since each letter was sent.
fda <- fda %>%
  mutate(days_elapsed = Sys.Date() - issued,
          weeks_elapsed = difftime(Sys.Date(), issued, units = "weeks"))

# Join to identify doctors paid to run Expert-led forums who also received a warning letter.
expert_warned_inner <- inner_join(pfizer, fda, by=c("first_name" = "name_first", "last_name" = "name_last")) %>%
  filter(category=="Expert-Led Forums")

expert_warned_semi <- semi_join(pfizer, fda, by=c("first_name" = "name_first", "last_name" = "name_last")) %>%
  filter(category=="Expert-Led Forums")

# As above, but select desired columns from data
expert_warned <- inner_join(pfizer, fda, by=c("first_name" = "name_first", "last_name" = "name_last")) %>%
  filter(category=="Expert-Led Forums") %>%
  select(first_plus, last_name, city, state, total, issued)

expert_warned <- inner_join(pfizer, fda, by=c("first_name" = "name_first", "last_name" = "name_last")) %>%
  filter(category=="Expert-Led Forums") %>%
  select(2:5,10,12)

# Load disease and democracy data.
disease_democ <- read_csv("data/wcsj/disease_democ.csv")

# Map values in data to X and Y axes.
ggplot(disease_democ, aes(x = infect_rate, y = democ_score))

# Customize axis labels.
ggplot(disease_democ, aes(x = infect_rate, y = democ_score)) +
  xlab("Infectious disease prevalence score") +
  ylab("Democratization score")

# Change the theme.
ggplot(disease_democ, aes(x = infect_rate, y = democ_score)) +
  xlab("Infectious disease prevalence score") + 
  ylab("Democratization score") +
  theme_minimal(base_size = 14, base_family = "Georgia")

# Save chart template, and plot.
disease_democ_chart <- ggplot(disease_democ, aes(x = infect_rate, y = democ_score)) +
  xlab("Infectious disease prevalence score") + 
  ylab("Democratization score") +
  theme_minimal(base_size = 14, base_family = "Georgia")

# Plot saved chart template.
plot(disease_democ_chart)

# Add a layer with points.
disease_democ_chart +
  geom_point()

# Themed scatterplot
ggplot(disease_democ, aes(x = infect_rate, y = democ_score)) +
  xlab("Infectious disease prevalence score") + 
  ylab("Democratization score") +
  theme_minimal(base_size = 14, base_family = "Georgia") +
  geom_point()

# Add a trend line.
disease_democ_chart +
  geom_point() +
  geom_smooth()

# Customize the two geom layers.
disease_democ_chart +
  geom_point(size = 3, alpha = 0.5) +
  geom_smooth(method = lm, se=FALSE, color = "#FF0000")

# Customize again, coloring the points by income group.
disease_democ_chart +
  geom_point(size = 3, alpha = 0.5, aes(color = income_group)) +
  geom_smooth(method = lm, se = FALSE, color = "black", linetype = "dotdash", size = 0.3)

# Color the entire chart by income group.
ggplot(disease_democ, aes(x = infect_rate, y = democ_score, color=income_group)) +
  xlab("Infectious disease prevalence score") + 
  ylab("Democratization score") +
  theme_minimal(base_size = 14, base_family = "Georgia") + 
  geom_point(size = 3, alpha = 0.5) +
  geom_smooth(method=lm, se=FALSE, linetype= "dotdash", size = 0.3)

disease_democ_chart +
  geom_point(size = 3, alpha = 0.5, aes(color = income_group)) +
  geom_smooth(method = lm, se = FALSE, color = "black", linetype = "dotdash", size = 0.3) +
  scale_x_continuous(limits=c(0,60)) +
  scale_y_continuous(limits=c(0,100)) +
  scale_color_brewer(palette = "Set1",
                     name="Income group",
                     breaks=c("High income: OECD","High income: non-OECD","Upper middle income","Lower middle income","Low income"))

# Save final disease and democracy chart.
final_disease_democ_chart <- disease_democ_chart +
  geom_point(size = 3, alpha = 0.5, aes(color = income_group)) +
  geom_smooth(method = lm, se = FALSE, color = "black", linetype = "dotdash", size = 0.3) +
  scale_x_continuous(limits=c(0,60)) +
  scale_y_continuous(limits=c(0,100)) +
  scale_color_brewer(palette = "Set1",
                     name="Income group", 
                     breaks=c("High income: OECD","High income: non-OECD","Upper middle income","Lower middle income","Low income"))

# Load data.
food_stamps <- read_csv("data/wcsj/food_stamps.csv")

# Save basic chart template.
food_stamps_chart <- ggplot(food_stamps, aes(x = year, y = participants)) +
  xlab("Year") +cl
  ylab("Participants (millions)") +
  theme_minimal(base_size = 14, base_family = "Georgia")

# line chart
food_stamps_chart +  
  geom_line()

# Customize the line, add a title.
food_stamps_chart +
  geom_line(size = 1.5, color = "red") +
  ggtitle("Line chart")

# Add a second layer to make a dot-and-line chart.
food_stamps_chart +
  geom_line() +
  geom_point() +
  ggtitle("Dot-and-line chart")
