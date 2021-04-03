# GMIT Programming and Scripting Project 2021
# Author: Sam Tracey

# Exploratory Data Analysis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import dataframe_image as dfi
import seaborn as sns
import scipy.stats as stats
from sklearn.linear_model import LinearRegression



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

dfi.export(data.describe(), "table_1.png")

# Splitting the data set by species of flower and describing the data for each group individually then saving to folder as png.
setosa = data.loc[data.species== "setosa",:]
dfi.export(setosa.describe(), "table_2.png")
versicolor = data.loc[data.species== "versicolor",:]
dfi.export(versicolor.describe(), "table_3.png")
virginica = data.loc[data.species== "virginica",:]
dfi.export(virginica.describe(), "table_4.png")



# Exploratory Data Analysis - Data Visualization - reference for mean markers on Zotero
# Plotting boxplots for each column using a for loop to iterate through all columns in the data set (except species)
sns.set(style="darkgrid")

for column in data.columns[:4]:  # Loop over all columns except 'Species'
    sns.set()
    fig, ax = plt.subplots()
    sns.set(style="ticks")
    sns.boxplot(x='species',
            y=column,                                       # column is chosen from iris data set based on loop iteration
            data=data, 
            order=["versicolor", "virginica", "setosa"],
            showmeans = True, 
            meanprops={"marker":"o",
                       "markerfacecolor":"white", 
                       "markeredgecolor":"black",
                       "markersize":"10"})

    # sns.boxplot(x='species', y=column, data=data)  # column is chosen here
    sns.despine(offset=10, trim=True)
    plt.title('Box Plot of {}'.format(column), fontsize=20)
    fig.set_size_inches(8, 8)
    plt.savefig('Boxplot_of_{}.png'.format(column), dpi=300)  # filename based on column name in Iris Data set




# KDE plots using for loop
for column in data.columns[:4]:  # Loop over all columns except 'Species'
    sns.set()
    fig, ax = plt.subplots()  
    sns.kdeplot(data=data, x=column, hue="species")    
    plt.title('Kernal Density Estimation (KDE) Plot of {}'.format(column), fontsize=20)
    fig.set_size_inches(8, 8)
    plt.savefig('KDE_of_{}.png'.format(column), dpi=300)  # filename based on column name in Iris Data set




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
plt.savefig("Distribution_plot_Setosa.png", bbox_inches="tight", dpi=300)            # reference available in zotero


#Examining correlation of petals and Sepals
# reference for data.corr function: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html
dfi.export(data.corr(method = 'pearson'), "table_5.png")
dfi.export(setosa.corr(method = 'pearson'), "table_6.png")
dfi.export(virginica.corr(method = 'pearson'), "table_7.png")
dfi.export(versicolor.corr(method = 'pearson'), "table_8.png")

# visualising correlations for each species - note setosa is an outlier.

sns.pairplot(data, hue='species', palette="OrRd")
plt.savefig("pairplot_by_species.png", dpi=300)



sns.lmplot(x='sepal length', y='sepal width', data = data, hue = 'species', markers =[".", "x", "+"])
plt.xlim(left=4, right=8)
plt.savefig("regression_plot_sepal.png", bbox_inches="tight", dpi=300)

sns.lmplot(x='petal length', y='petal width', data = data, hue = 'species', markers =[".", "x", "+"])
plt.xlim(left=0.7, right=7)
plt.savefig("regression_plot_petal.png", bbox_inches="tight", dpi=300)





