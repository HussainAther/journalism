# World Conference of Science Journalists 2017 R for Data Journalism workshop

* `fda.csv`: Data on warning letters sent to doctors by the U.S. Food and Drug Administration, because of problems in the way in which they ran clinical trials testing experimental treatments. Contains the following variables:

    - `name_last` `name_first` `name_middle`: Doctor’s last, first, and middle names.
    - `issued`: Date letter was sent.
    - `office`: Office within the FDA that sent the letter.
    - `disease_democ.csv`: Data illustrating a controversial theory suggesting that the emergence of democratic political systems has depended largely on nations having low rates of infectious disease, from the [Global Infectious Diseases and Epidemiology Network](http://www.gideononline.com/) and _[Democratization: A Comparative Analysis of 170 Countries](http://www.amazon.com/Democratization-Comparative-Analysis-Countries-Routledge/dp/0415318602)_.

* `food_stamps.csv`: [U.S. Department of Agriculture data](http://www.fns.usda.gov/pd/supplemental-nutrition-assistance-program-snap) on the number of `participants`, in millions, and `costs`, in $ billions, of the federal Supplemental Nutrition Assistance Program from 1969 to 2016.

* `kindergarten.csv`: Data from the [California Department of Public Health](https://data.chhs.ca.gov/dataset/school-immunizations-in-kindergarten-by-academic-year), documenting enrollment and the number of children with complete immunizations at entry into kindergartens in California from 2001 to 2015. Contains the following variables:

    - `district`: School district.
    - `sch_code`: Unique identifying code for each school.
    - `pub_priv`: Whether school is public or private.
    - `school`: School name.
    - `enrollment`: Number of children enrolled.
    - `complete`: Number of children with complete immunizations.
    - `start_year`: Year of entry (for the 2015-2016 school year, for example, this would be 2015).

* `nations.csv`: Data from the [World Bank Indicators](http://data.worldbank.org/indicator/all) portal, which is an incredibly rich resource. Contains the following variables, from 1990 onwards:

    - `iso2c` `iso3c`: Two- and Three-letter [codes](http://www.nationsonline.org/oneworld/country_code_list.htm) for each country, assigned by the [International Organization for Standardization](http://www.iso.org/iso/home/store/catalogue_tc/catalogue_detail.htm?csnumber=63545).
    - `country`: Country name.
    - `year`
    - `population`: Estimated [total population](http://data.worldbank.org/indicator/SP.POP.TOTL) at mid-year, including all residents apart from refugees.
    - `gdp_percap`: [Gross Domestic Product per capita](http://data.worldbank.org/indicator/NY.GDP.PCAP.PP.CD) in current international dollars, corrected for purchasing power in different territories.
    - `life_expect`: [Life expectancy at birth](http://data.worldbank.org/indicator/SP.DYN.LE00.IN), in years.
    - `population`: Estimated total population at mid-year, including all residents apart from refugees.
    - `birth_rate`: [Live births during the year per 1,000 people](http://data.worldbank.org/indicator/SP.DYN.LE00.IN), based on mid-year population estimate.
    - `neonat_mortal_rate`: [Neonatal mortality rate](http://data.worldbank.org/indicator/SH.DYN.NMRT): babies dying before reaching 28 days of age, per 1,000 live births in a given year.
    - `region` `income`: World Bank [regions](http://siteresources.worldbank.org/DATASTATISTICS/Resources/CLASS.XLS) and income groups, explained [here](http://data.worldbank.org/about/country-and-lending-groups).

* `pfizer.csv`: Payments made by Pfizer to doctors across the United States in the second half on 2009. Contains the following variables:

    - `org_indiv`: Full name of the doctor, or their organization.
    - `first_plus`: Doctor’s first and middle names.
    - `first_name` `last_name`: First and last names.
    - `city` `state`: City and state.
    - `category of payment`: Type of payment, which include `Expert-led Forums`, in which doctors lecture their peers on using Pfizer’s drugs, and `Professional Advising.
    - `cash`: Value of payments made in cash.
    - `other`: Value of payments made in-kind, for example puschase of meals.
    - `total`: value of payment, whether cash or in-kind.

* `simulations.csv` : Data from NASA simulations of historical temperatures, estimating the effect of natural and human influences on climate, processed from the [raw data](https://www.bloomberg.com/graphics/2015-whats-warming-the-world/data/forcings.csv) used for this [piece from Bloomberg News](https://www.bloomberg.com/graphics/2015-whats-warming-the-world/).
    - `year`
    - `type` : Natural or Human
    - `value` : Global average temperature from the simulation, relative to average simulated value from 1990-2000. 

* `warming.csv` : [National Oceanic and Atmospheric Administration](https://www.ncdc.noaa.gov/cag/global/time-series/globe/land_ocean/ytd/12/1880-2017.csv) data on the annual average global temperature, from 1880 to 2017.
    - `year`
    - `value` : Average global temperature, compared to average from 1900-2000.
