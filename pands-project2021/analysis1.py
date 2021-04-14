# GMIT Programming and Scripting Project 2021
# Author: Sam Tracey

# Import the necessary libraries
from contextlib import redirect_stdout
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import dataframe_image as dfi
import seaborn as sns
import scipy.stats as stats
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression




# First step is to read the iris.csv file in as a dataframe called data.
# we then assign column headers for aesthetics.
# Finally we display the summary statistics to the screen
data = pd.read_csv('iris.csv')
data.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'species']
print ('\n' * 3)
print ('\t\t********** Summary Statistics **********')
print ('\n')
print (data.describe())


# reference: https://realpython.com/python-data-cleaning-numpy-pandas/
print('Check Each Columns to Ensure no Missing Data\n')
print(data.isnull().sum())


# dataframe_image.export allows us to save the output of the summarydata.describe as a .png file
# reference: https://stackoverflow.com/a/63387275

dfi.export(data.describe(), 'table_1.png')

# Splitting the data set by species of flower and describing the data for each group individually then saving to folder as png.
setosa = data.loc[data.species== 'setosa',:]
dfi.export(setosa.describe(), 'table_2.png')
versicolor = data.loc[data.species== 'versicolor',:]
dfi.export(versicolor.describe(), 'table_3.png')
virginica = data.loc[data.species== 'virginica',:]
dfi.export(virginica.describe(), 'table_4.png')



# Exploratory Data Analysis - Data Visualization - reference for mean markers on Zotero
# Plotting boxplots for each column using a for loop to iterate through all columns in the data set (except species)
sns.set(style='darkgrid')

for column in data.columns[:4]:  # Loop over all columns except 'Species'
    sns.set()
    fig, ax = plt.subplots()
    sns.set(style='ticks')
    sns.boxplot(x='species',
            y=column,                                       # column is chosen from iris data set based on loop iteration
            data=data, 
            order=['versicolor', 'virginica', 'setosa'],
            showmeans = True, 
            meanprops={'marker':'o',
                       'markerfacecolor':'white', 
                       'markeredgecolor':'black',
                       'markersize':'10'})

    # sns.boxplot(x='species', y=column, data=data)  # column is chosen here
    sns.despine(offset=10, trim=True)
    plt.title('Box Plot of {}'.format(column), fontsize=20)
    fig.set_size_inches(8, 8)
    plt.savefig('Boxplot_of_{}.png'.format(column), dpi=300)  # filename based on column name in Iris Data set
plt.close()



# KDE plots using for loop
for column in data.columns[:4]:  # Loop over all columns except 'Species'
    sns.set()
    fig, ax = plt.subplots()  
    sns.kdeplot(data=data, x=column, hue='species')    
    plt.title('Kernal Density Estimation (KDE) Plot of {}'.format(column), fontsize=20)
    fig.set_size_inches(8, 8)
    plt.savefig('KDE_of_{}.png'.format(column), dpi=300)  # filename based on column name in Iris Data set
plt.close('all')                                          # Since this block creates 4 separate graphs we used close all to shut them all down.



# Normality testing each individual species - reference saved for D'Agostino's K2 Test for normality
# reference: https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/
print('\nFor Setosa Species:\n')
for param in ['sepal length', 'sepal width', 'petal length', 'petal width']:
    z, pval = stats.normaltest(setosa[param])
    if(pval < 0.05):
        print('%s has a p-value of %f - distribution is not normal' % (param, pval))
    else:
        print('%s has a p-value of %f' % (param, pval))

print('\nFor Virginica Species:\n')
for param in ['sepal length', 'sepal width', 'petal length', 'petal width']:
    z, pval = stats.normaltest(virginica[param])
    if(pval < 0.05):
        print('%s has a p-value of %f - distribution is not normal' % (param, pval))
    else:
        print('%s has a p-value of %f' % (param, pval))

print('\nFor Versicolor Species:\n')
for param in ['sepal length', 'sepal width', 'petal length', 'petal width']:
    z, pval = stats.normaltest(versicolor[param])
    if(pval < 0.05):
        print('%s has a p-value of %f - distribution is not normal' % (param, pval))
    else:
        print('%s has a p-value of %f' % (param, pval))

sns.displot(setosa, x='petal width', kde=True)              
plt.title('Further Examination of Setosa Distribution', fontsize=14)
plt.savefig('Distribution_plot_Setosa.png', bbox_inches='tight', dpi=300)            # reference available in zotero
plt.close()

#Examining correlation of petals and Sepals
# reference for data.corr function: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html
dfi.export(data.corr(method = 'pearson'), 'table_5.png')
dfi.export(setosa.corr(method = 'pearson'), 'table_6.png')
dfi.export(virginica.corr(method = 'pearson'), 'table_7.png')
dfi.export(versicolor.corr(method = 'pearson'), 'table_8.png')

# visualising correlations for each species - note setosa is an outlier.

sns.pairplot(data, hue='species', palette='OrRd')
plt.savefig('pairplot_by_species.png', dpi=300)
plt.close()


sns.lmplot(x='sepal length', y='sepal width', data = data, hue = 'species', markers =['.', 'x', '+'])
plt.xlim(left=4, right=8)
plt.savefig('regression_plot_sepal.png', bbox_inches='tight', dpi=300)
plt.close()

sns.lmplot(x='petal length', y='petal width', data = data, hue = 'species', markers =['.', 'x', '+'])
plt.xlim(left=0.7, right=7)
plt.savefig('regression_plot_petal.png', bbox_inches='tight', dpi=300)
plt.close()


# Regression analysis. Reference: https://towardsdatascience.com/the-complete-guide-to-linear-regression-in-python-3d3f8f06bf8
# Reference: https://realpython.com/linear-regression-in-python/

x = data['petal width'].values.reshape(-1,1)                # Reshape both x and y data to create two dimensional arrays required for regression modeling
y = data['petal length'].values.reshape(-1,1)
x1 = data['sepal width'].values.reshape(-1,1)
y1 = data['sepal length'].values.reshape(-1,1)



reg_model = LinearRegression().fit (x,y)                   # Create an instance of the class LinearRegression representing the regression model and fit the model            
# reg_model.fit (x,y)                                         
predictions = reg_model.predict(x)                         # Obtain the predicted response for petal width and petal length
reg_model1 = LinearRegression().fit (x1,y1)                # Create a second instance of the class LinearRegression representing the regression model and fit the model               
#reg_model1.fit (x1,y1)
predictions1 = reg_model1.predict(x1)                      # Obtain the predicted response for sepal width and sepal length 

# reference: https://towardsdatascience.com/the-complete-guide-to-linear-regression-in-python-3d3f8f06bf8

plt.scatter(x, y, c = 'blue')                              # use plt scatterplot to visualise the fitted regression model on the petal data 
plt.plot(x, predictions, c = 'red')
plt.xlabel('Petal Width')
plt.ylabel('Petal Length')
plt.title('Regression Analysis of Petal Width Versus Petal Length')
plt.savefig('regression_analysis_petal.png', bbox_inches='tight', dpi=300)
plt.close()


plt.scatter(x1, y1, c = 'blue')                            # use plt scatterplot to visualise the fitted regression model on the sepal data   
plt.plot(x1, predictions1, c = 'red')
plt.xlabel('Sepal Width')
plt.ylabel('Sepal Length')
plt.title('Regression Analysis of Sepal Width Versus Sepal Length')
plt.savefig('regression_analysis_sepal.png', bbox_inches='tight', dpi=300)
plt.close()


# reference : https://www.statsmodels.org/stable/gettingstarted.html

X = data['petal length']                            # define the x axis data for ordinary least squared (OLS) regression)
y = data['petal width']                             # define the y axis data for ordinary least squared (OLS) regression)
X2 = sm.add_constant(X)                             # add a column of 1s so that model has an intercept
model = sm.OLS(y, X2)                               # Describe OLS regression model (Linear regression)
results = model.fit()                               # Fit the OLS regression model


# reference : https://docs.python.org/3/library/contextlib.html#contextlib.redirect_stdout
with open('petal_model_summary.txt', 'w') as f:     # redirecting the output of the model summary to a txt file
    with redirect_stdout(f):
        print(results.summary())


X = data['sepal length']                            # define the x axis data for ordinary least squared (OLS) regression)                          
y = data['sepal width']                             # define the y axis data for ordinary least squared (OLS) regression)
X2 = sm.add_constant(X)                             # add a column of 1s so that model has an intercept
model = sm.OLS(y, X2)                               # Describe OLS regression model (Linear regression)
results = model.fit()                               # Fit the OLS regression model

with open('sepal_model_summary.txt', 'w') as f:     # redirecting the output of the model summary to a txt file
    with redirect_stdout(f):
        print(results.summary())