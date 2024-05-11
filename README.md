# Introduction
This is a a data exploratory data analysis in which i try to understand the World's population. I try to find countries with the highest population, their population densities and to find continents with the highest pupulation numbers. I also try to find how population is correlated with the country's area.

Check the original dataset here:
[World Population Data](/dataset/world_population.csv)

Check the Pythone code here:
[Code](/code_1.py)

# What is Exploratory Data Analysis
Exploratory data analysis (EDA) is used  to analyze and investigate data sets and summarize their main characteristics, often employing data visualization methods.

EDA helps determine how best to manipulate data sources to get the answers you need, making it easier to identify patterns, spot anomalies, test a hypothesis, or check assumptions.

### The questions answered in the Analysis
1. How is the data distributed?
2. Draw a Box plot to show the distribution of data and identify outliers
3. What are the top 5 countries with the highest Population?
4. How is population correlated to the country's area and country's growth rate?
5. What are the continental averages for each attribute?
6. Draw a Graph to show the continental population averages from 1970 to 2022


# Tools I Used
VS Code and Juypter Notebooks

# Libraries used
1. pandas (for data manipulation)
2. seaborn (for data visualizations)
3. matplotlib (for interactive and static visualizations)
4. numpy (for working with numerical data)

# The Analysis
The analysis was aimed on understanding the data and knowing how it is distributed.

## Importing the Libraries
 Imported the libraries i was to use:

 ```python
 import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np
 ```

## Importing the data into the Notebook
The next step was to import the dataset and save it into a dataframe (**df**)

 ```python
 df = pd.read_csv(r"C:\Users\User\Desktop\tinashe beans. Data Nerd\Exploratory Data Analysis in Pandas\dataset\world_population.csv")
df
 ```
![[Imported csv as dataframe (df)]](/Picures/1.original_df.png)
*Imported csv as dataframe (df)*

 ## How is the data distributed?
 This started by running the functions like **.info()**, **.describe()**, **.isnull()** and **.nunique()**. This was to understand the dataset I was working with. Below is the code and the results:

## .info()
 ```python
 #getting infomation ie data types, the columns and the memory about the data set
df.info()
 ```
 ![[.info]](/Picures/2.info.png)
 
*infomation of the dataset and its attributes*

## .describe()
 ```python
 #getting the statistical infomation (Mean, min, max, standard deviation etc) for the values in the dataframe
print(df.describe())
 ```
 ![[.info]](/Picures/3.describe.png)

*Discrptive stats for the dataset*

## .isnull()
 ```python
#Printing the number of null values
print(df.isnull().sum())
 ```
 ![[.isnull]](/Picures/4.num_of_nulls.png)

*number of null values in each column*

## .nunique()
 ```python
#printing all the unique values
print(df.nunique())
 ```
 ![[.nunique]](/Picures/5.uniques.png)

*number of unique values in each column*

## Draw a Box plot to show the distribution of data and identify outliers
I used the **.boxplot()** function to create a box plot.

```python
df.boxplot()
```
 ![[boxplot]](/Picures/boxplot.png)

*boxplot*


##  What are the top 5 countries with the highest Population?
I used the **.sort()** function to sort the dataframe by the values in the **2022 Population** column. Then arranged the values in descending order.

 ```python
#sorting the datframe by population to find the top 5 countries with the highest population
df.sort_values(by=['2022 Population'], ascending=False, inplace= True)
df.head()
 ```
 ![top 5](/Picures/6.top%205.png)
*top 5 countries by population*

**Results:** **China** as per 2022 results, it has the highest population. Followed by **India**, **USA**, **Indonesia** and **Pakstan**, in that order.

##  How is population correlated to the country's area, country's growth rate and other attributes?
To answer this question I used the **.corr** function to create a correlation matrix.

 ```python
# finding the correlation between the Population values
numeric_columns = df.select_dtypes(include=[np.number])
correlation_matrix = numeric_columns.corr
print(correlation_matrix())
 ```
 ![[corr1]](/Picures/corr1.png)

*correlation matrix 1*

 ![[corr2]](/Picures/corr2.png)

*correlation matrix 2*

 ![[corr3]](/Picures/corr3.png)

*correlation matrix 3*

To help understand the data from the correlation matrix i created a heat map to visualise the data easily. I used the **plt.show()** to create the heatmap

 ```python
#drawing a heat map to show the correlation between attibutes
sns.heatmap(correlation_matrix(), annot= True)
plt.rcParams['figure.figsize'] = (20,7)
plt.show()
 ```
 ![[corr1]](/Picures/heatmap.png)
*correlation matrix 1*

**Results:** Population and area have a correlation value of 0. That means they any increase in area or a decrease in are does no affect the Population.

# What are the continental population averages from 1970 to 2022?
I used the **.groupby** function to group the data by the **Continent** Column and defined the columns I wanted to be in my datframe (df1) i.e Population figures from 1970 to 2022. I then used the **.mean()** function to calculate the population averages for each year. Then sorted the resulting values in Descending order.

```python
#continental averages from the highest population to the lowest
df1 = df.groupby('Continent')[['1970 Population',
       '1980 Population', '1990 Population', '2000 Population',
       '2010 Population', '2015 Population', '2020 Population',
       '2022 Population']].mean(numeric_only=True).sort_values(by=['2022 Population'], ascending=False)
df1
```
 ![[continental averages]](/Picures/averages.png)
*continental averages*


# Draw a Graph to show the continental population averages from 1970 to 2022
Inorder to do this i first had to sort my datframe in a way that would make vizualization easy and for it to make sense. So I used the **.transpose()** function to change the columns into rows.

```python

#changing the columns to become the index or rows
df2 = df1.transpose()
df2
```
 ![[transposed]](/Picures/transposed.png)
*transposed*

Then i used Matplot to plot the graph
```python
df2.plot()
```
 ![[graph]](/Picures/graph.png)
*graph of yearly population by continent*

# Insights
1.  There is a slight decrease in population in Asia from 1970 t0 1980. THis is beacause of some countries, like India's Kerala state and China achieved lower birth rates through increased marriage age, while others like Thailand and Taiwan saw a rise in contraceptive use.

2. There was sharp increase in Population in Asia from 1990 to 2000. This is beacause of low mortality rates and improved health facilities.

3. From 2000 to 2022 there haas been a steady increase in population in Asia due to the controlled fertility laws eg One child policy in China and the Singapore that tried to maintain the population growth rate at a minimum. Also due to the increased level of education of women. 

4. Other continents like Africa, Europe, North and South America have a steady growth in population.


