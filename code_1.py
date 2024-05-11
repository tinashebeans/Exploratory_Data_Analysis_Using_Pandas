#Importing the necessary libraries
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r"C:\Users\User\Desktop\tinashe beans. Data Nerd\Exploratory Data Analysis in Pandas\dataset\world_population.csv")
df

#getting infomation about the data set
df.info()

#getiing the statistical infomation for the values in the dataframe
print(df.describe())

#Printing the number of null values that are in each column
print(df.isnull().sum())

#printing the number all the unique values
print(df.nunique())

#sorting the datframe by population to find the top 5 countries with the highest population
df.sort_values(by=['2022 Population'], ascending=False, inplace= True)
df.head()

# finding the correlation between the Population values
numeric_columns = df.select_dtypes(include=[np.number])
correlation_matrix = numeric_columns.corr
print(correlation_matrix())

#drawing a heat map to show the correlation
sns.heatmap(correlation_matrix(), annot= True)
plt.rcParams['figure.figsize'] = (20,7)
plt.show()

#continental averages from the highest population to the lowest
df1 = df.groupby('Continent')[['1970 Population',
       '1980 Population', '1990 Population', '2000 Population',
       '2010 Population', '2015 Population', '2020 Population',
       '2022 Population']].mean(numeric_only=True).sort_values(by=['2022 Population'], ascending=False)
df1

#changing the columns to become the index (rows)
df2 = df1.transpose()
df2

#plotting the dataframe for easier trend visualisation of data using Matplotlib
df2.plot()

#creating a box plot to see the distribution of data and find outliers
df.boxplot()

