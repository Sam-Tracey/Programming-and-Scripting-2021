# GMIT Programming and Scripting Project 2021
# Author: Sam Tracey

# Exploratory Data Analysis

import pandas as pd
import matplotlib.pyplot as plt
import dataframe_image as dfi
import seaborn as sns


# First step is to read the iris.csv file in as a dataframe called data.
# we then assign column headers for aesthetics.
data = pd.read_csv('iris.csv')
data.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'species']
#print (data.describe())
# print(data)

# reference: https://realpython.com/python-data-cleaning-numpy-pandas/
print("Check Each Columns to Ensure no Missing Data\n")
print(data.isnull().sum())


# dataframe_image.export allows us to save the output of the summarydata.describe as a .png file
# reference: https://stackoverflow.com/a/63387275
# reference for data.corr function: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html

dfi.export(data.describe(), "table_1.png")

# Creating sub groups for each species of flower and describing the data for each group individually then saving to folder as png.
setosa = data.loc[data.species== "setosa",:]
dfi.export(setosa.describe(), "table_2.png")
versicolor = data.loc[data.species== "versicolor",:]
dfi.export(versicolor.describe(), "table_3.png")
virginica = data.loc[data.species== "virginica",:]
dfi.export(virginica.describe(), "table_4.png")


# Exploratory Data Analysis - Data Visualization - reference for mean markers on Zotero
# Boxplots using subplots to reduce number of images from 4 to 1.
sns.set(style="darkgrid")
fig, axs = plt.subplots(2, 2, figsize=(10, 10))             # https://matplotlib.org/3.1.0/gallery/subplots_axes_and_figures/subplots_demo.html

sns.boxplot(x='species',
            y='sepal length', 
            data=data, 
            order=["versicolor", "virginica", "setosa"],
            showmeans = True, 
            meanprops={"marker":"o",
                       "markerfacecolor":"white", 
                       "markeredgecolor":"black",
                       "markersize":"10"}, ax=axs[0, 0])
sns.boxplot(x='species',
            y='sepal width', 
            data=data, 
            order=["versicolor", "virginica", "setosa"],
            showmeans = True, 
            meanprops={"marker":"o",
                       "markerfacecolor":"white", 
                       "markeredgecolor":"black",
                       "markersize":"10"}, ax=axs[0, 1])
sns.boxplot(x='species',
            y='petal length', 
            data=data, 
            order=["versicolor", "virginica", "setosa"],
            showmeans = True, 
            meanprops={"marker":"o",
                       "markerfacecolor":"white", 
                       "markeredgecolor":"black",
                       "markersize":"10"}, ax=axs[1, 0])
sns.boxplot(x='species',
            y='petal width', 
            data=data, 
            order=["versicolor", "virginica", "setosa"],
            showmeans = True, 
            meanprops={"marker":"o",
                       "markerfacecolor":"white", 
                       "markeredgecolor":"black",
                       "markersize":"10"}, ax=axs[1, 1])
plt.suptitle("Boxplots of Petal and Sepal Width and Length", size = 20)     # https://www.delftstack.com/howto/matplotlib/how-to-set-a-single-main-title-for-all-the-subplots-in-matplotlib/
plt.savefig("Image_1.png")



# KDE plots using subplots to reduce number of images from 4 to 1.

fig, axs = plt.subplots(2, 2, figsize=(10, 10))

sns.kdeplot(data=data, x="sepal length", hue="species", ax=axs[0, 0])
sns.kdeplot(data=data, x="sepal width", hue="species", ax=axs[0, 1])
sns.kdeplot(data=data, x="petal length", hue="species", ax=axs[1, 0])
sns.kdeplot(data=data, x="petal width", hue="species", ax=axs[1, 1])
plt.suptitle("Kernal Density Estimation (KDE)", size = 20)
plt.savefig("Image_2.png")


# dfi.export(data.corr(method = 'pearson'), "table_2.png")



# sns_plot = sns.pairplot(data, hue='species', palette="OrRd")

# sns_plot.savefig("Image_1.png")

