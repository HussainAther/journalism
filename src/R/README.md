# R scripts

Run these R scripts to analyze data. Take apart knowledge, skills, and abilities (KSA) as they relate to data science jobs and research.
These files require input `.tsv` files, tab-separated value files that have data science information in rows separated by tabs. `.tsv` files
can generally be exported from software such as Microsoft Excel.

* `techdict.R` : This script creates a technology dictionary for skills and education required for data science jobs. 
    - Usage: `R techdict.R dspos.tsv` 
    - Requirements: [dplyr](https://anaconda.org/r/r-dplyr), [gdata](https://anaconda.org/anaconda/gdata), [ggplot2](https://anaconda.org/r/r-ggplot2), [tidyr](https://anaconda.org/r/r-tidyr).
    - Uses gdata, dplyr, and tidyr for manipulating and cleaning data and ggplot2 for plotting. 

* `wcsj.R` : This script plots the data from the World Conference of Science Journalists (WCSJ) 2017 workshop R for Data Journalism. 
    - Usage: `R wcsj.R`
    - Requirements: dplyr, ggplot2, [readr](https://anaconda.org/conda-forge/r-readr), [tidyverse](https://anaconda.org/r/r-tidyverse)
    - Uses dplyr for processing data, ggplot2 and tidyverse for plotting, and readr for reading and writing files.

* `yearexp.R` : This script plots the number of data science job postings for minimum years and educational requirements for an input `tsv` file.
    - Usage: `R yearexp.R exp.tsv`
    - Requirements: dplyr, tidyr, ggplot2. 
    - Uses dplyr and tidyr for manipulating and cleaning data and ggplot2 for plotting. 
