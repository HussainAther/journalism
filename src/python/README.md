# Python scripts

Run these python scripts to analyze data. Each python script begins with `import` statements that let the user import functions and modules from various classes. Then there are lines that are separated by `"""`. These lines are commented out.

* In `arc`, `arcread.py` and `arcread2.py`: These scripts read the input ArcGIS files.
    - Usage: `python arcread.py`
    - Requirements: [arcpy](https://anaconda.org/esri/arcpy).

* In `citation`, `citeToCSV.py` : This script converts a list of citations into a readable .csv with a panda DataFrame as a middle product.
    - Usage: `python citeToCSV.py citationsfile`  
      - For example: `python citetocsv.py ../../data/citation/statllcpub.txt`
    - Requirements: [pandas](https://anaconda.org/anaconda/pandas), [matplotlib](https://anaconda.org/conda-forge/matplotlib).
    - Input files must end with a suffix (such as .txt) and follow the "Scientific Style and Format for Authors, Editors, and Publishers" format. 
    - Comments in the input files must begin with #.
    - Uses pandas as a method of storing and manipulating data with DataFRames and matplotlib for plotting graphs.

  * `people.py` : This script is an example for using pandas on manipulating data.
    - Usage: `python people.py`
    - Requirements: pandas.
    - Uses pandas for data manipulation.

* In `criticalmaterials`, `correlation.py`, `graph.py`, `periodic.py`, `prepare.py` and `table.py` : These scripts produce graphs of critical minerals across the world. 
    - Usage: `python src/python/criticalminerals/graph.py`
    - Requirements: [bokeh](https://anaconda.org/bokeh/bokeh), [geopandas](https://anaconda.org/conda-forge/geopandas), [geoplot](https://anaconda.org/conda-forge/geoplot), [numpy](https://anaconda.org/anaconda/numpy), [pyshp](https://anaconda.org/conda-forge/pyshp). 
    - Uses the input shapefile in `data/criticalminerals`.
    - A periodic table of the critical minerals can be found here: https://hussainather.com/2019/12/15/global-mapping-mineral-trends/

* In `curricula`, `curriculaAnalysis.py` : This script analyzes the Data Science curricula across universities. 
    - Usage: `python curriculaAnalysis.py`
    - Requirements: pandas, matplotlib.
    - Uses the curricula `.csv` files in the `data/curricula` directory as input.

* In `dam`, `read.py` : This script analyzes the Oregon dam inventory data.
    - Usage: `python src/python/dam/read.py`
    - Requirements: numpy, pandas.
    - Uses the `oregondams.csv` file in `data/dam` as input.

* In `deeplearning`, `overview.html` : Load this in your web browser to view a tutorial on deep learning with scikit-learn. You can also use Jupyter notebook to view the `overview.ipynb` file. To do this, you need to install [jupyter[(https://anaconda.org/anaconda/jupyter). Then run `jupyter-notebook` in your command line to start the notebook server. Navigate to the `overview.ipynb` file to view it in a reader-friendly format.

* In `defaunation`, `graphy.py` : This creates graphs of the various studies used in _Gardner et al., 2019_.
    - Usage: `python src/python/defaunation/graph.py`
    - Requirements: matplotlib, numpy, pandas.

  * `stat.py` : Testing some statistics functions on the paper. 
    - Usage: `python src/python/defaunation/stat.py`
    - Requirements: matplotlib, numpy, pandas, [researchpy](https://anaconda.org/researchpy/researchpy).

* In `foia`, `read.py` : This reads through the FOIA contacts and prints a view of the top records.
    - Usage: `python src/python/foia/read.py`
    - Requirements: pandas.

* In `food`, `poverty.py` : This reads the poverty statistics from the U.S. Bureau of the Census, Current Population Survey "Income and Poverty in the United States: 2016" report.
    - Usage: `python src/python/food/poverty.py`
    - Requirements: matplotlib, numpy, pandas.

* In `franciscan`, `read.py` : Read the JSON file of crust formation data of the Western Cordillera (Franciscan equivalents) and print it in DataFrame form. 
    - Usage: `python src/python/franciscan/read.py`
    - Requirements: [json](https://anaconda.org/jmcmurray/json), pandas.

* In `geocode`, `jsonread.py` : Read the JSON file to automate geocoding.
    - Usage: `python src/python/geocode/jsonread.py`
    - Requirements: geopandas, json.

* In `geophysical`, `grd.py` : Generic script to read a .grd file.
    - Usage: `python src/python/geophysical/grd.py`

* In `googlemap`, `geochart.py` : Visualize a map of disposable median monthly salary per country on the world map projection using Google Geochart and Table Visualization.
    - Usage: `python src/python/googlemap/geochart.py`
    - Requirements: [gviz_api](https://pypi.org/project/gviz-api/).
    - Output stored as `output/googlemap/output.html`.
 
* In `map`, `cartoread.py` : SQL script with code for creating interactive maps using Carto.

* In `medicare`, `read.py` : This reads in medicare data.
    - Usage: `python src/python/medicare/read.py`
    - Requirements: pandas.

* In `mineral`, `mine.py`, `mineplant.py`, `shapefileread.py`, `specificmine.py`, `uscopper.py`, `usmanganese.py`, and `usplatinum.py` : These scripts analyze the active mines and mineral plants in the US 
    - Usage: `python src/python/mineral/mine.py`
    - Requirements: [basemap](https://anaconda.org/anaconda/basemap), [chart_studio](https://anaconda.org/plotly/chart-studio), [ipython](https://anaconda.org/anaconda/ipython), matplotlib, numpy, pandas, [plotly](https://anaconda.org/plotly/plotly), [pyshp](https://anaconda.org/conda-forge/pyshp).
    - Output stored in `output/mineral`.

  * `svm.py` : This script creates a decision boundary as part of a support vector machine (SVM) in classifying the data.
    - Usage: `python src/python/mineral/svm.py`
    - Requirements: geopandas, matplotlib, numpy, pandas, [scikit-learn](https://anaconda.org/anaconda/scikit-learn), [seaborn](https://anaconda.org/anaconda/seaborn). 

* In `misc`, `makewordcloud.py` : This script makes a word cloud for a given set of text input from an input file hardcoded into the script.
    - Usage: `python src/python/misc/makewordcloud.py`
    - Requirements: [nltk](https://anaconda.org/anaconda/nltk), [wordcloud](https://anaconda.org/conda-forge/wordcloud).
    - This script is written to be as succinct and concise, using as few lines of code as possible.
    - A full explanation is found here: https://hussainather.com/2019/12/17/make-a-word-cloud-in-a-single-line-of-python/

  * `uncertainty.py` : This script has simple statistics tests for evaluating uncertainty.
    - Usage: `python uncertainty.py`
    - Requirements: matplotlib, numpy.

  * `visualizeDataset.py` : This script creates an example dataset and plots it.
    - Usage: `python visualizeDataset.py`
    - Requirements: matplotlib, pandas, seaborn. 
    - Uses matplotlib and seaborn for plotting and pandas for data manipulation.

* In `nicr`, `table.py` and `usmap.py` : These scripts create maps and tables of Ni-Cr deposits across the US and the world.
    - Usage: `python src/python/nicr/table.py`
    - Requirements: matplotlib, numpy, pandas.

  * `svm.py` : This script uses a support vector machine (SVM) to extract information and draw trends from platinum-group elements (PGE) with nickel and chromium mineralization. 
    - Usage: `python src/python/nicr/svm.py`
    - Requirements: matplotlib, numpy, pandas, scikit-learn.

* In `postings`, `extractInfo.py` : This script extracts additional info from the raw input data.
    - Usage: `python extractInfo.py`
    - Requirements: pandas, matplotlib.
    - Input zip files can be downloaded from https://www.dropbox.com/sh/713fruhtcqlj28s/AAAIFwRfcrGL4leUlsJzVhgGa?dl=0 
    - You must have unzipped the `raw.zip` file and `postings.csv.zip` in `data/postings` before running.

  * `dataSkills.py` : This script establishes the scaffolding of data skills.
    - Usage: `python dataSkills.py`
    - Requirements: pandas.
  * `latentAnalysis.py` : This script performs latent analysis of the semantics of the job descriptions.
    - Usage: `python latentAnalysis.py`
    - Requirements: [gensim](https://anaconda.org/anaconda/gensim), [ipython](https://anaconda.org/anaconda/ipython), [keras](https://anaconda.org/conda-forge/keras), matplotlib, nltk, pandas, [pyLDAvis](https://anaconda.org/conda-forge/pyldavis), [basemap](https://anaconda.org/anaconda/basemap), scikit-learn], [seaborn](https://anaconda.org/anaconda/seaborn), [stop_words](https://anaconda.org/conda-forge/r-stopwords), wordcloud. 
    - Input zip files can be downloaded from https://www.dropbox.com/sh/713fruhtcqlj28s/AAAIFwRfcrGL4leUlsJzVhgGa?dl=0 
    - You must have unzipped the `raw.zip` file and `postings.csv.zip` in `data/postings` before running.
    - Uses gensim, nltk, pLDAvis, scikit-learn, and stop_words to perform the analysis, pandas for data manipulation, and matplotlib, seaborn, and wordcloud for plotting.

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

* In `rock`, `read.py` : This reads data on igneous rocks in the US extracted from the PLUTO database.
    - Usage: `python src/python/rock/read.py`
    - Requirements: geopandas, matplotlib, pandas.

* In `santacruz/airborne`, `csvread.py` : This maps the csv files of magnetic and radiometric of Santa Cruz.
    - Usage: `python src/python/santacruz/airborne/csvread.py`
    - Requirements: matplotlib, numpy, pandas, seaborn.
    
  * `knn.py`, `lr.py`, and `svm.py` : These three scripts perform k-nearest neighbors clustering, logistic regression, and support vector machine classification.
    - Usage: `python src/python/santacruz/airborne/knn.py`
    - Requirements: matplotlib, pandas, seaborn, scikit-learn.

* In `santacruz/asbestos`, `read.py` : This reads and maps asbestos mines.
    - Usage: `python src/python/santacruz/asbestos/read.py`
    - Requirements: geopandas, matplotlib, pandas, [shapely](https://anaconda.org/conda-forge/shapely).

* In `santacruz/usmin`, `read.py` : This maps historical USGS topographic maps of the Santa Cruz area.
    - Usage: `python src/python/santacruz/usmin/read.py`
    - Requirements: geopandas, matplotlib, numpy.

* In `santacruz/volc`, `volc.py` : This reads data on tertiary granitic rocks in the area.
    - Usage: `python src/python/santacruz/volc/volc.py`
    - Requirements: json, pandas. 

* In `slack`, `analyze.py` : This analyzes the slack statistics (or slacktistics, if I may).
    - Usage: `python src/python/slack/analyze.py`
    - Requirements: matplotlib, numpy, pandas.

* In `twitter`, `tweetread.py` : This reads tweets from accounts with a consumer key `ckey`, consumer secret `csecret`, access token `atoken`, access secret `asecret`, and keyword file `kwfile`. 
    - Usage: `python src/python/twitter/tweetread.py ckey csecret atoken asecret kwfile`
    - Requirements: json, [tweepy](https://anaconda.org/conda-forge/tweepy). 
    - In order to use all of this though, we need to setup a Developer API acocunt with Twitter and create an application to get credentials. Review the video for instructions on how to do this or if you are already familiar with it, just get the credentials from https://apps.twitter.com/.
    
    `network.py` : For creating a network and communities for a given `keyword` and `image` file. The script uses the `keyword` as the word to search through Twitter and the `image` as the image on which to lay the word cloud.
    - Usage: `python keyword image`
    - Requirements: [i-graph](https://anaconda.org/conda-forge/python-igraph), json, maplotlib, [networkx](https://anaconda.org/anaconda/networkx), numpy, pandas, [PIL](https://anaconda.org/anaconda/pil), [postgresql](https://anaconda.org/anaconda/postgresql), [pycorenlp](https://pypi.org/project/pycorenlp/), seaborn, [tqdm](https://anaconda.org/conda-forge/tqdm), tweepy, wordcloud.
