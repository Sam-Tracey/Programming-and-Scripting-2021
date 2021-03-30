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
data.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']
#print (data.describe())
# print(data)

# reference: https://realpython.com/python-data-cleaning-numpy-pandas/
print("Check Each Columns to Ensure no Missing Data\n")
print(data.isnull().sum())


# dataframe_image.export allows us to save the output of the summarydata.describe as a .png file
# reference: https://stackoverflow.com/a/63387275
# reference for data.corr function: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html

dfi.export(data.describe(), "table_1.png")


# Exploratory Data Analysis - Data Visualization - reference for mean markers on Zotero


sns.set(style="darkgrid")
sns.boxplot(x='class',
            y='sepal length', 
            data=data, 
            order=["versicolor", "virginica", "setosa"],
            showmeans = True, 
            meanprops={"marker":"o",
                       "markerfacecolor":"white", 
                       "markeredgecolor":"black",
                       "markersize":"10"})
                       
plt.title("Sepal Length by Iris Class", size = 16)
plt.savefig("Image_1.png")
plt.close()


sns.set(style="darkgrid")
sns.boxplot(x='class',
            y='sepal width', 
            data=data, 
            order=["versicolor", "virginica", "setosa"],
            showmeans = True, 
            meanprops={"marker":"o",
                       "markerfacecolor":"white", 
                       "markeredgecolor":"black",
                       "markersize":"10"})
                       
plt.title("Sepal Width by Iris Class", size = 16)
plt.savefig("Image_2.png")
plt.close()


sns.set(style="darkgrid")
sns.boxplot(x='class',
            y='petal length', 
            data=data, 
            order=["versicolor", "virginica", "setosa"],
            showmeans = True, 
            meanprops={"marker":"o",
                       "markerfacecolor":"white", 
                       "markeredgecolor":"black",
                       "markersize":"10"})
                       
plt.title("Petal Length by Iris Class", size = 16)
plt.savefig("Image_3.png")
plt.close()


sns.set(style="darkgrid")
sns.boxplot(x='class',
            y='petal width', 
            data=data, 
            order=["versicolor", "virginica", "setosa"],
            showmeans = True, 
            meanprops={"marker":"o",
                       "markerfacecolor":"white", 
                       "markeredgecolor":"black",
                       "markersize":"10"})
                       
plt.title("Petal Width by Iris Class", size = 16)
plt.savefig("Image_4.png")
plt.close()


# KDE plots. The reference for adjusting the subplot margins is in Zotero

sns.displot(data,  x="sepal length", hue="class", kind="kde", fill = True)
plt.title("Sepal Length Kernal Density Estimation (KDE)", size = 16)
plt.subplots_adjust(top=0.8)
plt.savefig("Image_5.png")
plt.close()

sns.displot(data,  x="sepal width", hue="class", kind="kde", fill = True)
plt.title("Sepal Width Kernal Density Estimation (KDE)", size = 16)
plt.subplots_adjust(top=0.8)
plt.savefig("Image_6.png")
plt.close()

sns.displot(data,  x="petal length", hue="class", kind="kde", fill = True)
plt.title("Petal Length Kernal Density Estimation (KDE)", size = 16)
plt.subplots_adjust(top=0.8)
plt.savefig("Image_7.png")
plt.close()

sns.displot(data,  x="petal width", hue="class", kind="kde", fill = True)
plt.title("Petal Width Kernal Density Estimation (KDE)", size = 16)
plt.subplots_adjust(top=0.8)
plt.savefig("Image_8.png")
plt.close()
# dfi.export(data.corr(method = 'pearson'), "table_2.png")



# sns_plot = sns.pairplot(data, hue='class', palette="OrRd")

# sns_plot.savefig("Image_1.png")

