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

# Make bubble chart.
ggplot(nations2016, aes(x = gdp_percap, y = life_expect)) +
  xlab("GDP per capita") +
  ylab("Life expectancy at birth") +
  theme_minimal(base_size = 14, base_family = "Georgia") +
  geom_point(aes(size = population, color = region), alpha = 0.7) +
  scale_size_area(guide = FALSE, max_size = 15) +
  scale_x_continuous(labels = dollar) +
  stat_smooth(formula = y ~ log10(x), se = FALSE, size = 0.5, color = "black", linetype="dotted") +
  scale_color_brewer(name = "", palette = "Set2") +
  theme(legend.position=c(0.8,0.4))

# Animate entire time series with gganimate.
nations_plot <- ggplot(nations, aes(x = gdp_percap, y = life_expect)) +
  xlab("GDP per capita") +
  ylab("Life expectancy at birth") +
  theme_minimal(base_size = 14, base_family = "Georgia") +
  geom_point(aes(size = population, color = region), alpha = 0.7) +
  scale_size_area(guide = FALSE, max_size = 15) +
  scale_x_continuous(labels = dollar) +
  stat_smooth(formula = y ~ log10(x), se = FALSE, size = 0.5, color = "black", linetype="dotted") +
  scale_color_brewer(name = "", palette = "Set2") +
  theme(legend.position=c(0.8,0.4)) +
  # gganimate code
  ggtitle("{frame_time}") +
  transition_time(year) +
  ease_aes("linear") +
  enter_fade() +
  exit_fade()

animate(nations_plot)

# Save as a GIF.
animate(nations_plot, fps = 10, end_pause = 30, width = 750, height = 450)
anim_save("output/animation/nations.gif")

# Save as a video.
animate(nations_plot, renderer = ffmpeg_renderer(), fps = 30, duration = 20, width = 800, height = 450)
anim_save("output/animation/nations.mp4")

# Load data.
warming <- read_csv("data/wcsj/warming.csv")

# Draw chart.
warming_plot <- ggplot(warming, aes(x = year, y = value)) +
  geom_line(colour="black") +
  geom_point(shape = 21, colour = "black", aes(fill = value), size=5, stroke=1) +
  scale_x_continuous(limits = c(1880,2017)) +
  scale_y_continuous(limits = c(-0.5,1)) +
  scale_fill_distiller(palette = "RdYlBu", limits = c(-1,1), guide = FALSE) +
  xlab("") +
  ylab("Difference from 1900-2000 (ºC)") +
  theme_minimal(base_size = 16, base_family = "Georgia")
