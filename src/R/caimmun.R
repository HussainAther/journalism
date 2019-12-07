# load required packages
library(dplyr)
library(readr)
library(ggplot2)
library(scales)

# function to convert any text string into proper case
toproper <- function(x) {
  sapply(x, function(strn)
  { s <- strsplit(strn, "\\s")[[1]]
  paste0(toupper(substring(s, 1,1)), 
         tolower(substring(s, 2)),
         collapse=" ")}, USE.NAMES=FALSE)
}

# import CA kindergarten immunization data and calculate incomplete rate by county
immun <- read_tsv("data/vacc/kindergarten.tsv") %>%
  mutate(county=toproper(county),
         district=toproper(district),
         school=toproper(school),
         pub_priv=toproper(pub_priv),
         incomplete_pc=100-complete_pc,
         sch_code=as.character(sch_code),
         prejan_pbe=as.integer(prejan_pbe),
         prejan_pbe_pc=as.numeric(prejan_pbe_pc),
         doc_couns_pbe=as.integer(doc_couns_pbe),
         doc_couns_pbe_pc=as.numeric(doc_couns_pbe_pc),
         relig_pbe=as.integer(relig_pbe),
         relig_pbe_pc=as.numeric(relig_pbe_pc))


write_csv(immun, "data/vacc/kindergarten.csv")

# identify counties with the largest enrollment
immun_counties <- immun %>%
  group_by(county) %>%
  summarize(enrolled=sum(enrollment, na.rm=TRUE)) %>%
  arrange(desc(enrolled)) 

top5 <- head(immun_counties,5) %>%
  select(county)

# percent incomplete, entire state, by year
immun_year <- immun %>%
  group_by(start_year) %>%
  summarize(enrolled=sum(enrollment, na.rm=TRUE),complete=sum(complete, na.rm=TRUE)) %>%
  mutate(pc_incomplete=round(((enrolled-complete)/enrolled),4))

immun_2016 <- read_csv("data/vacc/ca_immun_2016.csv") %>%
  mutate(pc_incomplete = round(pc_incomplete,4))
        
immun_year <- bind_rows(immun_year, immun_2016)


# percent incomplete, by county, by year
immun_counties_year <- immun %>%
  group_by(county,start_year) %>%
  summarize(enrolled=sum(enrollment, na.rm=TRUE),complete=sum(complete, na.rm=TRUE)) %>%
  mutate(pc_incomplete=round(((enrolled-complete)/enrolled),4))

# percent incomplete, top 5 counties by enrollment, by year
immun_top5_year <- inner_join(immun_counties_year,top5)

# bar chart by year, entire state
ggplot(immun_year, aes(x=start_year, y=pc_incomplete)) %>%
  + geom_bar(stat="identity", fill="#8e0152", alpha=0.8) %>%
  + theme_minimal() %>%
  + theme_minimal(base_family="Proxima Nova Semibold") %>%
  + scale_y_continuous(labels = scales::percent) %>%
  + scale_x_continuous(breaks = c(2004,2008,2012,2016)) %>%
  + xlab("Entry year") %>%
  + ylab("") %>%
  # + ggtitle("Immunization in California kindergartens, entire state") %>%
  + theme(panel.grid.major.x = element_blank(),
          panel.grid.minor.x = element_blank(),
          text=element_text(size=14))

# dot and line chart by year
ggplot(immun_year, aes(x=start_year, y=pc_incomplete)) %>%
  + geom_line(size=1, color="red") %>%
  + geom_point(size=3, color="red") %>%
  + theme_minimal() %>%
  + scale_y_continuous(labels = scales::percent, limits=c(0,0.1)) %>%
  + scale_x_continuous(breaks = c(2002,2004,2006,2008,2010,2012,2014)) %>%
  + xlab("") %>%
  + ylab("Incomplete") %>%
  + ggtitle("Immunization in California kindergartens, entire state") %>%
  + theme(text=element_text(size=16))

# line chart by year
ggplot(immun_year, aes(x=start_year, y=pc_incomplete)) %>%
  + geom_line(size=1.5, color="red") %>%
  + theme_minimal() %>%
  + scale_y_continuous(labels = scales::percent, limits=c(0.06,0.1)) %>%
  + scale_x_continuous(breaks = c(2002,2004,2006,2008,2010,2012,2014)) %>%
  + xlab("") %>%
  + ylab("Incomplete") %>%
  + ggtitle("Immunization in California kindergartens, entire state") %>%
  + theme(text=element_text(size=16))

# dot and line chart, top5 counties, by year
ggplot(immun_top5_year, aes(x=start_year, y=pc_incomplete, color=county)) %>%
  + scale_color_brewer(palette = "Set1", name = "") %>%
  + geom_line(size=1) %>%
  + geom_point(size=3) %>%
  + theme_minimal() %>%
  + scale_y_continuous(labels = scales::percent, limits = c(0,0.15)) %>%
  + scale_x_continuous(breaks = c(2002,2004,2006,2008,2010,2012,2014)) %>%
  + xlab("") %>% 
  + ylab("Incomplete") %>%
  + theme(legend.position="bottom") %>%
  + ggtitle("Immunization in California kindergartens\n(five largest counties)") %>%
  + theme(text=element_text(size=16))


# dot and line chart, all counties, by year
ggplot(immun_counties_year, aes(x=start_year, y=pc_incomplete, color=county)) %>%
  + geom_line(size=1) %>%
  + geom_point(size=3) %>%
  + theme_minimal() %>%
  + theme(legend.position="none") %>%
  + scale_y_continuous(labels = scales::percent) %>%
  + scale_x_continuous(breaks = c(2002,2004,2006,2008,2010,2012,2014)) %>%
  + xlab("") %>%
  + ylab("Incomplete") %>%
  + ggtitle("Immunization in California kindergartens, by county") %>%
  + theme(text=element_text(size=16))
  
# heat map, all counties, by year
ggplot(immun_counties_year, aes(x=start_year, y=county)) %>%
  + geom_tile(aes(fill = pc_incomplete), colour = "white") %>%
  + scale_fill_gradient(low = "white", 
                        high = "red", name="", 
                        labels = scales::percent) %>%
  + scale_x_continuous(breaks = c(2002,2004,2006,2008,2010,2012,2014)) %>%
  + theme_minimal() %>%
  + xlab("") %>%
  + ylab("County") %>%
  + theme(panel.grid.major = element_blank(),
          panel.grid.minor = element_blank(),
          legend.position="bottom",
          legend.key.height = unit(0.4, "cm"),
          text=element_text(size=14)) %>%
  + ggtitle("Immunization in California kindergartens, by county")

# show all schools, by year
ggplot(immun, aes(x=start_year, y=incomplete_pc/100)) %>%
  + geom_point(position="jitter", 
               color="red", 
               alpha=0.1, 
               aes(size=enrollment)) %>%
  + scale_color_gradient(low = "white", high = "red") %>%
  + scale_x_continuous(breaks = c(2002,2004,2006,2008,2010,2012,2014)) %>%
  + scale_y_continuous(labels = scales::percent) %>%
  + theme_minimal() %>%
  + xlab("") %>%
  + ylab("Incomplete") %>%
  + guides(size=guide_legend(title="Enrollment")) %>%
  + ggtitle("Immunization in California kindergartens") %>%
  + theme(panel.grid.major.x = element_blank(),
          panel.grid.minor.x = element_blank(),
          legend.position="bottom",
          text=element_text(size=16))

# import 2016-2016 county data for major shots, and combine with historical data

shots_county_2016 <- read_csv("kindergarten2016.csv") %>%
  mutate(county=toproper(county),
         year="2016-17",
         start_year=2016,
         dtp_pc=round(dtp/enrollment*100, 2),
         polio_pc=round(polio/enrollment*100, 2),
         mmr_pc=round(mmr/enrollment*100, 2),
         hepb_pc=round(hepb/enrollment*100, 2),
         vari_pc=round(vari/enrollment*100, 2))

shots_county <- immun %>%
  group_by(county, start_year, year) %>%
  summarise(enrollment = sum(enrollment, na.rm=T),
            dtp = sum(dtp, na.rm=T),
            polio = sum(polio, na.rm=T),
            mmr = sum(mmr, na.rm=T),
            hepb = sum(hepb, na.rm=T),
            vari = sum(vari, na.rm=T)) %>%
  mutate(dtp_pc=round(dtp/enrollment*100, 2),
         polio_pc=round(polio/enrollment*100, 2),
         mmr_pc=round(mmr/enrollment*100, 2),
         hepb_pc=round(hepb/enrollment*100, 2),
         vari_pc=round(vari/enrollment*100, 2))

shots_county <- bind_rows(shots_county,shots_county_2016) %>%
  mutate(dtp_performance=dtp_pc-95,
         mmr_performance=mmr_pc-95,
         hepb_performance=hepb_pc-95,
         vari_performance=vari_pc-95)

counties <- shots_county %>%
  ungroup() %>%
  select(county) %>%
  unique() %>%
  mutate(order = c(1:58))

shots_county = inner_join(shots_county, counties)

# set color palette and sequence of values to apply it to
pal <- c("#8e0152","#c51b7d","#de77ae","#f1b6da","#fde0ef","#f7f7f7","#b8e186")
vals <- seq(-25, 5, length = 20)

# heat map, dtp, by year
ggplot(shots_county, aes(x=start_year, y=reorder(county,-order))) + 
  geom_tile(aes(fill = dtp_performance), colour = "white") + 
  scale_fill_gradientn("Deviation from\n95% target",
                       colors = pal, 
                       values = vals, 
                       rescaler = function(x, ...) x, 
                       oob = identity) +
  scale_x_continuous(breaks = c(2004,2008,2012,2016)) +
  # theme_minimal(base_size=12) +
  theme_minimal(base_size=14, base_family="Proxima Nova Semibold") +
  xlab("Entry year") + 
  ylab("") + 
  # ggtitle("Diptheria-Tetanus-Pertussis") +
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        legend.position="bottom",
        legend.text=element_text(size = 8))

# heat map, mmr, by year
ggplot(shots_county, aes(x=start_year, y=reorder(county,-order))) + 
  geom_tile(aes(fill = mmr_performance), colour = "white") + 
  scale_fill_gradientn("Deviation from\n95% target",colors = pal, values = vals, rescaler = function(x, ...) x, oob = identity) +
  scale_x_continuous(breaks = c(2004,2008,2012,2016)) +
  # theme_minimal(base_size=14) +
  theme_minimal(base_size=14, base_family="Proxima Nova Semibold") +
  xlab("Entry year") + 
  ylab("") + 
  # ggtitle("Measles-Mumps-Rubella") +
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        legend.position="bottom",
        legend.text=element_text(size = 8))

# extra code for ucsc plotly class
immun_counties_year <- immun_counties_year %>%
  mutate(pc_incomplete=pc_incomplete*100)

write.csv(immun_counties_year,"data/vacc/ca_vacc_counties.csv", row.names = F, na="")





