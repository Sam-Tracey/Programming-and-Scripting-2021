![Index GMIT](media/47d94fa74dbb3b94dce1e246799237ad.png)

| Name: Sam Tracey                               |
|------------------------------------------------|
| Student Number: G00398245                      |
| Course: Programming and Scripting Project 2021 |
| Tutor: Andrew Beatty                           |

# 

# Introduction

This repository has been created to document my project work for the 2021
Programming and scripting module as part of a Higher Diploma in Data Analytics
with Galway and Mayo Institute of Technology.

Currently in my place of employment, Minitab 18 is used extensively for all data
analysis at a cost of €1709.70 per license [1]. This project concerns the
well-known Fisher’s Iris data set [2] and how it can be analysed using
exploratory data analysis and regression analysis with the Python programming
language.

As Python has been developed under an OSI-approved Open Source license [3] it is
free to use and readily available to anyone. Being able to use Python for data
analysis has a large cost saving implication for my employer.

# The Iris Dataset.

![The Iris Dataset — A Little Bit of History and Biology \| by Yong Cui \|
Towards Data Science](media/63b5516414cfe15f96be4c997286ca5c.jpeg)

The Iris data set was first developed by British statistician Ronald Fisher in
1936\. It is a set of multivariate data quantifying the variation observed in
three related species of Iris flower: The Iris Setosa, Iris Virginica and Iris
Versicolor [4]. The data set has gained huge popularity in the programming and
machine learning communities with University of California Irvine going as far
as to claim it is the “best know database to be found in pattern recognition
literature” [5]

The data set itself is small but not trivial. Containing 150 unique observations
split evenly across the three species of Iris. For each observation there are
four distinct attributes detailed: Petal length, petal width, sepal length and
sepal width.

The popularity of the data set can be easily seen with a quick Google search. As
of writing there are current 42,600 entries on GitHub concerning the Iris data
set and a further 3836 entries on Kaggle.

Interestingly on both the UCI website where the data set is free to download and
on the Iris Data set Wikipedia page there is a reference to two mistakes that
exist in the data set stored online:

*“This data differs from the data presented in Fishers article (identified by
Steve Chadwick, spchadwick '@' espeedaz.net ). The 35th sample should be:
4.9,3.1,1.5,0.2,"Iris-setosa" where the error is in the fourth feature. The 38th
sample: 4.9,3.6,1.4,0.1,"Iris-setosa" where the errors are in the second and
third features.”*

Further investigation of Fisher’s paper [6] corroborated this statement and
there are mistakes on the 35th sample and 38th sample. For this body of work, I
amended the data set downloaded from University of California Irvine to match
Fisher’s data set as it was recorded originally.

# Methods

The following software, libraries and files were used throughout this project:

-   Python version 3.8.5 via Anaconda 2020.11

-   Minitab version 19

-   Visual Studio version 1.55.2

-   Numpy version 1.19.2

-   Pandas version 1.1.3

-   Matplotlib version 3.3.2

-   Dataframe-image version 0.1.1

-   Seaborn version 0.11.0

-   Scipy version 1.5.2

-   Statsmodels version 0.12.0

-   The Iris dataset imported from UCI at
    <https://archive.ics.uci.edu/ml/machine-learning-databases/iris/>

The purpose of this project is to compare the ability of Python and my company’s
current analytical software, Minitab 19, to performing exploratory data analysis
(EDA) and regression analysis to investigate the Iris data set.

# Exploratory Data Analysis

Exploratory data analysis or EDA for short is a term coined by American
mathematician John W Tukey to describe the act of looking at a data set to “see
what it seems to say” [7]. By using summary data, statistical graphics (such as
box plots, scatter plots and histograms for example) and other visualisation
techniques we attempt to investigate the data to understand patterns, detect
outliers and find interesting relationships amongst the variables [8].

The first part of analysis in both Minitab and Python is to load the data to be
analysed into the software. Minitab provides a GUI to browse for a file to open.
In Python we can read a comma-separated file into a Dataframe named ‘data’ using
only a single line of code and the built in functionality of the pandas library:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
data = pd.read_csv('iris.csv')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Having read the data to our Dataframe we then proceed to assign headers for each
column of the Dataset:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
data.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'species']
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

[1] Minitab (2021) *Single User Annual Subscription License.* Available at:
<https://store.minitab.com/781/purl-minitab> Accessed (04 April 2021)

[2] University of California Irvine (2021) *Iris* *Data Set* Available at:
(<https://archive.ics.uci.edu/ml/datasets/iris> Accessed (04 April 2021)

[3] Python (2021) *History and License* Available at:
<https://docs.python.org/3/license.html> Accessed (04 April 2021)

[4] Wikipedia (2021) *Iris Flower Data Set* Available at:
<https://en.wikipedia.org/wiki/Iris_flower_data_set> Accessed (13-April-2021)

[5] University of California Irvine (2021) *Iris Data Set* Available at:
(<https://archive.ics.uci.edu/ml/datasets/iris> Accessed (13 April 2021)

[6] Fisher,R.A. "The use of multiple measurements in taxonomic problems" Annual
Eugenics, 7, Part II, 179-188 (1936); also in "Contributions to Mathematical
Statistics" (John Wiley, NY, 1950) Available at:
https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1469-1809.1936.tb02137.x
Accessed (07 April 2021)

[7] Morgenthaler, S. (2009), Exploratory data analysis. WIREs Comp Stat, 1:
33-44. Available at: <https://doi.org/10.1002/wics.2> Accessed (14 April 2021)

[8] IBM (2020) *Exploratory Data Analysis*. Available at:
[https://www.ibm.com/cloud/learn/exploratory-data-analysis\#toc-what-is-ex-ofRUduQ6](https://www.ibm.com/cloud/learn/exploratory-data-analysis#toc-what-is-ex-ofRUduQ6)
Accessed (14 April 2021)
