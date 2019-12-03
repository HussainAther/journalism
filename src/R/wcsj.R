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
