# Journalism tools

Results summary can be found here: https://hussainather.com/2019/06/25/data-based-analysis-reveals-data-science-job-prospects/

These tools are for data journalists and other writers and researchers to use in reporting stories. The scripts are found in the corresponding language in the `src` directory. Data was obtained from Corey Seliger and Megan Sapp Nelson of Purdue University through the Purdue University Research Repository (PURR). The raw input data files are found in `data`, and the output files are created and stored in `output`.
 
## How to use these tools

0. Make sure you have python, R, and the appropriate packages installed for each script. See ["Installation"](#Installation) below for instructions.
1. Download this repository as a `.zip` file (from the "Clone or download" button in the top-right), and unzip it.
2. Identify and open the terminal emulator program on your computer. Mac and Linux systems come with Terminal installed, and Windows systems come with Console. If there isn’t one installed, download one online. 
3. Type `pwd` and press enter. This command shows what your current working directory is. Type `ls` to display which directories and files are in this current directory. To move to another directory, run `cd directory` in which "directory" is the name of the directory you’d like to move to. To move up a directory, run `cd ..`. To view a file run `less file` in which file is the name of the file, and use the arrow keys to move up and down. To exit `less`, type `q`. In the files, the code comments are on lines beginning with `#` or are separated off by `"""`. Comments are explanatory notes for anyone to use and understand the scripts. The script doesn't run lines that are commented out. They're only for anyone to leave notes in scripts.
2. Navigate to the unzipped directory. 
3. From there you can run the scripts from the directories in the `src` directory as instructed by the `README.md` files and the comments in the scripts. 

# Python scripts

Run these python scripts to analyze data. Each python script begins with `import` statements that let the user import functions and modules from various classes. Then there are lines that are separated by `"""`. These lines are commented out.

* `citeToCSV.py` : This script converts a list of citations into a readable .csv with a panda DataFrame as a middle product.
    - Usage: `python citeToCSV.py citationsfile`  
      - For example: `python citetocsv.py ../../data/citation/statllcpub.txt`
    - Requirements: [pandas](https://anaconda.org/anaconda/pandas), [matplotlib](https://anaconda.org/conda-forge/matplotlib).
    - Input files must end with a suffix (such as .txt) and follow the "Scientific Style and Format for Authors, Editors, and Publishers" format. 
    - Comments in the input files must begin with #.
    - Uses pandas as a method of storing and manipulating data with DataFRames and matplotlib for plotting graphs.

* `curriculaAnalysis.py` : This script analyzes the Data Science curricula across universities. 
    - Usage: `python curriculaAnalysis.py`
    - Requirements: pandas, matplotlib.
    - Uses the curricula `.csv` files in the `data/curricula` directory as input.

* `dataSkills.py` : This script establishes the scaffolding of data skills.
    - Usage: `python dataSkills.py`
    - Requirements: pandas.

* `extractInfo.py` : This script extracts additional info from the raw input data.
    - Usage: `python extractInfo.py`
    - Requirements: pandas, matplotlib.
    - Input zip files can be downloaded from https://www.dropbox.com/sh/713fruhtcqlj28s/AAAIFwRfcrGL4leUlsJzVhgGa?dl=0 
    - You must have unzipped the `raw.zip` file and `postings.csv.zip` in `data/postings` before running.

* `latentAnalysis.py` : This script performs latent analysis of the semantics of the job descriptions.
    - Usage: `python latentAnalysis.py`
    - Requirements: [gensim](https://anaconda.org/anaconda/gensim), [ipython](https://anaconda.org/anaconda/ipython), [keras](https://anaconda.org/conda-forge/keras), matplotlib, [nltk](https://anaconda.org/anaconda/gensimv), pandas, [pyLDAvis](https://anaconda.org/conda-forge/pyldavis), [basemap](https://anaconda.org/anaconda/basemap),[scikit-learn](https://anaconda.org/anaconda/scikit-learn), [seaborn](https://anaconda.org/anaconda/seaborn), [stop_words](https://anaconda.org/conda-forge/r-stopwords), [wordcloud](https://anaconda.org/conda-forge/wordcloud). 
    - Input zip files can be downloaded from https://www.dropbox.com/sh/713fruhtcqlj28s/AAAIFwRfcrGL4leUlsJzVhgGa?dl=0 
    - You must have unzipped the `raw.zip` file and `postings.csv.zip` in `data/postings` before running.
    - Uses gensim, nltk, pLDAvis, scikit-learn, and stop_words to perform the analysis, pandas for data manipulation, and matplotlib, seaborn, and wordcloud for plotting.

* `people.py` : This script is an example for using pandas on manipulating data.
    - Usage: `python people.py`
    - Requirements: pandas.
    - Uses pandas for data manipulation.

* `postingAnalysis.py` : This script analyzes the data science job postings across the United States. 
    - Usage: `python postingAnalysis.py`
    - This file must be run after running `extractInfo.py`.
    - Uses the `extracted.csv` file in the `output/postings` as input.
    - Requirements: [basemap](https://anaconda.org/anaconda/basemap), [numpy](https://anaconda.org/anaconda/numpy), matplotlib, pandas, [proj4](https://anaconda.org/conda-forge/proj), scikit-learn.
    - Uses numpy for numerical operations, pandas for data manipulation, scikit-learn for machine learning, and basemap and proj4 for plotting.

* `tfidf.py`: This script performs latent analysis by outputting word similarity and frequency statistics for a set of documents.
    - Usage: `python tfidf.py`
    - Requirements: gensim, matplotlib, numpy.
    - Input zip files can be downloaded from https://www.dropbox.com/sh/713fruhtcqlj28s/AAAIFwRfcrGL4leUlsJzVhgGa?dl=0 
    - You must have unzipped the `raw.zip` file and `postings.csv.zip` in `data/postings` before running.
    - Uses gensim for latent analysis and matplotlib and numpy for plotting. 

* `uncertainty.py` : This script has simple statistics tests for evaluating uncertainty.
    - Usage: `python uncertainty.py`
    - Requirements: matplotlib, numpy.

* `visualizeDataset.py` : This script creates an example dataset and plots it.
    - Usage: `python visualizeDataset.py`
    - Requirements: matplotlib, pandas, [seaborn](https://anaconda.org/anaconda/seaborn). 
    - Uses matplotlib and seaborn for plotting and pandas for data manipulation.

# R scripts

Run these R scripts to analyze data. Take apart knowledge, skills, and abilities (KSA) as they relate to data science jobs and research.
These files require input `.tsv` files, tab-separated value files that have data science information in rows separated by tabs. `.tsv` files
can generally be exported from software such as Microsoft Excel.

* `techdict.R` : This script creates a technology dictionary for skills and education required for data science jobs. 
    - Usage: `R techdict.R dspos.tsv` 
    - Requirements: [dplyr](https://anaconda.org/r/r-dplyr), [gdata](https://anaconda.org/anaconda/gdata), [ggplot2](https://anaconda.org/r/r-ggplot2),  [tidyr](https://anaconda.org/r/r-tidyr).
    - Uses gdata, dplyr, and tidyr for manipulating and cleaning data and ggplot2 for plotting. 

* `yearexp.R` : This script plots the number of data science job postings for minimum years and educational requirements for an input `tsv` file.
    - Usage: `R yearexp.R exp.tsv`
    - Requirements: dplyr, tidyr, ggplot2. 
    - Uses dplyr and tidyr for manipulating and cleaning data and ggplot2 for plotting. 

## Installation

The required packages are found in the `README.md` file in the directory for a corresponding language in the `src` directory. Packages can be installed using [anaconda](https://www.anaconda.com/). Anaconda is a package manager that lets you easily download packages using commands such as `conda install -c anaconda numpy` to, for example, install numpy or `conda install -c conda-forge matplotlib` to install matplotlib. Before installing packages, the corresopnding channels must be added with `conda config --add channels new_channel` in which `new_channel` is the name of the channel. The required channels are found on the conda page for the corresponding packages. The links to these pages are in the `README.md` files.

## Sources

Nelson, M. S. (2016). **Scaffolding for data management skills: From undergraduate education through postgraduate training and beyond**. Purdue University Research Repository. doi:10.4231/R7QJ7F9R

Seliger, C. S. (2018). **Data Scientist Postings and Data Science Curriculum Datasets**. Purdue University Research Repository. doi:10.4231/R7B27SJS

Seliger, C. S. (2018). **Regular Expression Dictionaries Derived from Data Scientist Positions and Course Curriculum**. Purdue University Research Repository. doi:10.4231/R7R78CGR

Seliger, C. S. (2018). **Text Mining and Plotting Tools for KSA / DS / HEI Research Study**. Purdue University Research Repository. doi:10.4231/R7MK6B49
