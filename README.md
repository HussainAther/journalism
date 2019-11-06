# Journalism tools

These tools are for data journalists and other writers and researchers to use in reporting stories. The scripts are found in the corresponding language in the `src` directory. The raw input data files are found in `data`, and the output files are created and stored in `output`.
 
## How to use these tools

0. Make sure you have python, R, and the appropriate packages installed for each script. See ["Installation"](#Installation) below for instructions.
1. Download this repository as a `.zip` file (from the "Clone or download" button in the top-right), and unzip it.
2. Identify and open the terminal emulator program on your computer. Mac and Linux systems come with Terminal installed, and Windows systems come with Console. If there isn’t one installed, download one online. 
3. Type `pwd` and press enter. This command shows what your current working directory is. Type `ls` to display which directories and files are in this current directory. To move to another directory, run `cd directory` in which "directory" is the name of the directory you’d like to move to. To move up a directory, run `cd ..`. To view a file run `less file` in which file is the name of the file, and use the arrow keys to move up and down. To exit `less`, type `q`. In the files, the code comments are on lines beginning with `#` or are separated off by `"""`. Comments are explanatory notes for anyone to use and understand the scripts. The script doesn't run lines that are commented out. They're only for anyone to leave notes in scripts.
2. Navigate to the unzipped directory. 
3. From there you can run the scripts from the directories in the `src` directory as instructed by the `README.md` files and the comments in the scripts. 

## Installation

The required packages are found in the `README.md` file in the directory for a corresponding language in the `src` directory. Packages can be installed using [anaconda](https://www.anaconda.com/). Anaconda is a package manager that lets you easily download packages using commands such as `conda install -c anaconda numpy` to, for example, install numpy or `conda install -c conda-forge matplotlib` to install matplotlib. Before installing packages, the corresopnding channels must be added with `conda config --add channels new_channel` in which `new_channel` is the name of the channel. The required channels are found on the conda page for the corresponding packages. The links to these pages are in the `README.md` files.

## Sources

Gardner, C.J., Bicknell, J.E., Baldwin-Cantello, W. et al. **Quantifying the impacts of defaunation on natural forest regeneration in a global meta-analysis**. _Nat Commun_ 10, 4590 (2019) doi:10.1038/s41467-019-12539-1

Nelson, M. S. (2016). **Scaffolding for data management skills: From undergraduate education through postgraduate training and beyond**. _Purdue University Research Repository_. doi:10.4231/R7QJ7F9R

Seliger, C. S. (2018). **Data Scientist Postings and Data Science Curriculum Datasets**. _Purdue University Research Repository_. doi:10.4231/R7B27SJS

Seliger, C. S. (2018). **Regular Expression Dictionaries Derived from Data Scientist Positions and Course Curriculum**. _Purdue University Research Repository_. doi:10.4231/R7R78CGR

Seliger, C. S. (2018). **Text Mining and Plotting Tools for KSA / DS / HEI Research Study**. _Purdue University Research Repository_. doi:10.4231/R7MK6B49
