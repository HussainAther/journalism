# Load libraries
library(easyGgplot2)
library(dplyr)
library(tidyr)

# Plot the number of job postings for minimum years of experience with an input .tsv file
# that has column values ("uuid", "explabel", "minyears", "bachelor", "master", "phd") 
# in which "uuid" is the Universal Unique Identifier, "explabel" is a description of experience,
# "minyears" is the minimum number of experience years, and the final three values are the educational
# requirements.

# Usage: "R yearexp.R exp.tsv" 
 
# Read commandline arguments.
args = commandArgs(trailingOnly=TRUE)

# Read the command-line argument as "tsvfile"
tsvfile = args[1]

# Check which directory we are in. If we're not in the main journalism
# directory, then cd to it.
while (sapply(strsplit(getwd(), "/"), tail, 1) != "journalism") {
    setwd("..")
}

# Read input .tsv file as a table
yrexp_degrees <- read.table(tsvfile,
                            header = FALSE, sep = "\t", quote = "", 
                            col.names = c("uuid", "explabel", "minyears", "bachelor", "master", "phd"), 
                            colClasses = c("factor", "character", "integer", "integer", "integer", "integer"),
                            skip = 1)

# Group the table by minimum year of years and save it as foo
foo <- yrexp_degrees %>% 
  group_by(minyears) %>% 
  summarize(bachelor = sum(bachelor),
            master = sum(master),
            phd = sum(phd))

# Caount the number of degrees required for each row of foo
foo2 <- as.data.frame(gather(foo, degree, count, `bachelor`:`phd`))

# Plot
plot <- foo2 %>%
  ggplot(aes(minyears, count, shape=degree, color=degree)) +
  scale_size(guide="none") + 
  geom_point(
    aes(
      minyears, count, shape=degree, color=degree, size=1
    )
  ) + 
  labs(x="Minimum Years of Experience", 
       y="Number of Job Postings",
       color="Degree Requirement", 
       shape="Degree Requirement") +
  geom_smooth(
    method="loess", 
    se=FALSE,
    show.legend=FALSE
    ) +
  guides(color = guide_legend(override.aes = list(size=4)))

# Check if the output file directory exists. If not, make it.
if (!file.exists("output/postings")){ 
    dir.create("output/postings"))
}

# Save the plot
ggsave(filename="output/postings/yearexp.png", plot=plot, width=8.45, height=5.08, dpi=300, units = "in")
