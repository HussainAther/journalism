# Load the libraries
library(gdata)
library(tidyr)
library(dplyr)
library(ggplot2)

# Create a technology dictionary for data science position information.
# Plot the number of job postings for minimum years of experience for an input .tsv
# that has columns values ("phrase", "entity", "dscount", "educount") that represent
# key KSA (Knowledge, skills, and abilities) phrases, the posting entity, count of data
# science skills, and count of educational skills, respectively.

# Usage: "R yearexp.R dspos.tsv"

# Read commandline arguments.
args = commandArgs(trailingOnly=TRUE)

# Read the command-line argument as "tsvfile".
tsvfile = args[1]

# Check which directory we are in. If we're not in the main journalism
# directory, then cd to it.
while (sapply(strsplit(getwd(), "/"), tail, 1) != "journalism") {
    setwd("..")
}

control_set <- read.table(tsvfile,
                          header = FALSE, sep = "\t", quote = "", 
                          col.names = c("phrase", "entity",
                                        "dscount", "educount"), 
                          colClasses = c("factor", "factor",
                                         "numeric", "numeric"),
                          skip = 1)

control_set[is.na(control_set)] <- 0

control_set$dspct <- control_set$dscount / sum(control_set$dscount) * 100
control_set$edupct <- control_set$educount / sum(control_set$educount) * 100
control_set$delta <- control_set$dspct - control_set$edupct 
control_set$absdelta <- abs(control_set$dspct - control_set$edupct)

# Traditional dual bar showing edupct and dspct positive.
control_set <- control_set[order(-control_set$absdelta),]

tbl2 <- gather(control_set, counttype, count, 
               dspct, edupct,
               factor_key = TRUE)

tbl2$phrase <- reorder.factor(tbl2$phrase, new.order=control_set$phrase)

tbl2 <- tbl2 %>%
  arrange(phrase)

# Plot.
plot <- ggplot(data=head(tbl2,50), 
       aes(
         x=reorder(phrase,absdelta), 
         y=count, 
         fill=counttype,
         width=0.7
       )
) +
  geom_bar(
    stat="identity", 
    color="black",
    position=position_dodge()
  ) +
  theme_minimal() + 
  scale_fill_manual(
    values = c("#999999", "#e69f00"), 
    labels=c(
      "DS Position Postings", 
      "DS Curricula"
    )
  ) +
  labs(
    y="Count Proportion", 
    x="KSA Phrases - Technology Dictionary (internally generated)", 
    fill = "Dataset"
  ) +
  coord_flip()

# Check if the output file directory exists. If not, make it.
if (!file.exists("output/postings")){
    dir.create("output/postings"))
}

# Save the plot.
ggsave(filename="/output/postings/techdict.png", plot=plot, width=8.45, height=5.08, dpi=300, units = "in")
write.table(control_set, "/output/postings/techdict.tsv", sep="\t")
