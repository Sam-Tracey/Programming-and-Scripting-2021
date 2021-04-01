# GMIT Programming and Scripting Project 2021
# Author: Sam Tracey

# Exploratory Data Analysis

import pandas as pd
import matplotlib.pyplot as plt
import dataframe_image as dfi
import seaborn as sns
import scipy.stats as stats



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

# Splitting the data set by species of flower and describing the data for each group individually then saving to folder as png.
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
plt.savefig("Image_1.png", dpi=300)



# KDE plots using subplots to reduce number of images from 4 to 1.

fig, axs = plt.subplots(2, 2, figsize=(10, 10))

sns.kdeplot(data=data, x="sepal length", hue="species", ax=axs[0, 0])
sns.kdeplot(data=data, x="sepal width", hue="species", ax=axs[0, 1])
sns.kdeplot(data=data, x="petal length", hue="species", ax=axs[1, 0])
sns.kdeplot(data=data, x="petal width", hue="species", ax=axs[1, 1])
plt.suptitle("Kernal Density Estimation (KDE)", size = 20)
plt.savefig("Image_2.png", dpi=300)

# Normality testing each individual species - reference saved for D'Agostino's K2 Test for normality
print("\nFor Setosa Species:\n")
for param in ["sepal length", "sepal width", "petal length", "petal width"]:
    z, pval = stats.normaltest(setosa[param])
    if(pval < 0.05):
        print("%s has a p-value of %f - distribution is not normal" % (param, pval))
    else:
        print("%s has a p-value of %f" % (param, pval))

print("\nFor Virginica Species:\n")
for param in ["sepal length", "sepal width", "petal length", "petal width"]:
    z, pval = stats.normaltest(virginica[param])
    if(pval < 0.05):
        print("%s has a p-value of %f - distribution is not normal" % (param, pval))
    else:
        print("%s has a p-value of %f" % (param, pval))

print("\nFor Versicolor Species:\n")
for param in ["sepal length", "sepal width", "petal length", "petal width"]:
    z, pval = stats.normaltest(versicolor[param])
    if(pval < 0.05):
        print("%s has a p-value of %f - distribution is not normal" % (param, pval))
    else:
        print("%s has a p-value of %f" % (param, pval))

sns.displot(setosa, x="petal width", kde=True)              
plt.title("Further Examination of Setosa Distribution", fontsize=14)
plt.savefig("Image_3.png", bbox_inches="tight", dpi=300)            # reference available in zotero


#Examining correlation of petals and Sepals

dfi.export(data.corr(method = 'pearson'), "table_5.png")
dfi.export(setosa.corr(method = 'pearson'), "table_6.png")
dfi.export(virginica.corr(method = 'pearson'), "table_7.png")
dfi.export(versicolor.corr(method = 'pearson'), "table_8.png")

sns_plot = sns.pairplot(data, hue='species', palette="OrRd")
sns_plot.savefig("Image_4.png", dpi=300)

