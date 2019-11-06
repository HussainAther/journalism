# Python scripts

Run these python scripts to analyze data. Each python script begins with `import` statements that let the user import functions and modules from various classes. Then there are lines that are separated by `"""`. These lines are commented out.

* In `arc`, `arcread.py` and `arcread2.py`: These scripts read the input ArcGIS files.
    - Usage: `python arcread.py`
    - Requirements: [arcpy](https://anaconda.org/esri/arcpy)

* In `citation`, `citeToCSV.py` : This script converts a list of citations into a readable .csv with a panda DataFrame as a middle product.
    - Usage: `python citeToCSV.py citationsfile`  
      - For example: `python citetocsv.py ../../data/citation/statllcpub.txt`
    - Requirements: [pandas](https://anaconda.org/anaconda/pandas), [matplotlib](https://anaconda.org/conda-forge/matplotlib).
    - Input files must end with a suffix (such as .txt) and follow the "Scientific Style and Format for Authors, Editors, and Publishers" format. 
    - Comments in the input files must begin with #.
    - Uses pandas as a method of storing and manipulating data with DataFRames and matplotlib for plotting graphs.

* In `criticalmaterials`, `graph.py`, `prepare.py` and `table.py` : These scripts produce graphs of critical minerals across the world.
    - Usage: `python src/criticalminerals/graph.py`
    - Requirements: [bokeh](https://anaconda.org/bokeh/bokeh), [geopandas](https://anaconda.org/conda-forge/geopandas), [geoplot](https://anaconda.org/conda-forge/geoplot), [numpy](https://anaconda.org/anaconda/numpy), [pyshp](https://anaconda.org/conda-forge/pyshp). 
    - Uses the input shapefile in `data/criticalminerals`.

* In `curricula`, `curriculaAnalysis.py` : This script analyzes the Data Science curricula across universities. 
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
    - Requirements: [basemap](https://anaconda.org/anaconda/basemap), numpy, matplotlib, pandas, [proj4](https://anaconda.org/conda-forge/proj), scikit-learn.
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
