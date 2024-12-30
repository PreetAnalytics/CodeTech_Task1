#!/usr/bin/env python
# coding: utf-8

import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt


df=pd.read_csv("C:/Users/harma/Desktop/Financial Sample.csv")


df.head()


df.columns


# Eliminating the white spaces 
df.columns = df.columns.str.strip()


df.columns

df.dtypes


# Changing the Datatypes 
num_col= ['Manufacturing Price','Sale Price','Gross Sales','Discounts','Sales','COGS','Profit']
for col in num_col:
    df[col] = df[col].astype(str)  # Convert to string if not already
    df[col] = df[col].replace({'\$': '', '₹': '', ',': ''}, regex=True)  # Remove currency symbols and commas
    df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert to numeric, replacing errors with NaN


# Changing data types to datatime 
df['Date'] = pd.to_datetime(df['Date'],errors='coerce')


# Changing  Data type to category 
Cat_col = ['Segment','Country','Product','Discount Band']
for col in Cat_col:
    df[col]=df[col].astype('category')


# reviewing the datatype 
df.dtypes


df.head()


# Checking for null values 
df.isnull().sum()


#filling the null values with 0
df['Profit'] = df['Profit'].fillna(0)


df.isnull().sum()


# Plotting histogram for Sales
sns.histplot(df['Sales'], bins=30, kde=True, color='blue')
plt.title('Sales Distribution')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()



sns.boxplot(x=df['Profit'])



# Kernel Density Estimate (kDE) to understand the Distribution of Discounts 
sns.kdeplot(df['Discounts'])


# Correlation Matrix to Understand the relationships between Variable 
correlation_matrix = df[['Units Sold', 'Sale Price', 'Gross Sales', 'Discounts', 'Sales', 'COGS', 'Profit']].corr()



sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')



# Checking For Outliers 

z_scores = np.abs((df['Profit'] - df['Profit'].mean()) / df['Profit'].std())
outliers = df[z_scores > 3]



Q1 = df['Profit'].quantile(0.25)
Q3 = df['Profit'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Profit'] < (Q1 - 1.5 * IQR)) | (df['Profit'] > (Q3 + 1.5 * IQR))]


# Total Sales By Segments 
sns.barplot(x='Segment', y='Sales', data=df)



# Total Profit By Country 
sns.barplot(x='Country', y='Profit', data=df)



# Total Sales By Month 
df.groupby('Month Name')['Sales'].sum().plot(kind='line')



# Profit Trend by Year 
sns.lineplot(x='Year', y='Profit', data=df)


# Relationship between Discount and Sales 
sns.scatterplot(x='Discounts', y='Sales', data=df)


# Relationship Betwween Sales and Profit 
sns.regplot(x='Sales', y='Profit', data=df)


# Pairwise Relationships Between Key Metrics 
sns.pairplot(df[['Units Sold', 'Sale Price', 'Gross Sales', 'Discounts', 'Sales', 'COGS', 'Profit']])