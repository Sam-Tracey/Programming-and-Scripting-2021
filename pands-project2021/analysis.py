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
dfi.export(data.corr(method = 'pearson'), "table_2.png")



sns_plot = sns.pairplot(data, hue='class', palette="OrRd")

sns_plot.savefig("Image_1.png")

