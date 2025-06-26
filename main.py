import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('.\Data\Input_Climate.csv')

#print(df.head())
#print(df.columns)

#Objectives:
#The objective of this tutorial is to become familiar with hydrologic data processing in R or Python. 
#The tutorial data is from the first Creek at Waterfall Hully catchment in South Australia. 
#The catchment is part of the Bureau of Meterology Hydrologic Reference Station network(...)

#Data:
#Input_Climate.csv:  
#This file contains 6 columns including climate zone identification key, date, maximum temperature, minimum temp, 
#rain, potential evapotranspiration and radiation. You can view the content of this file in EXCEL. 

#Data Processing:
#Upload the data in R or Python and prepare the following graphs or tables: 
#1. Visualize the daily mean temperature, and precipitation in the catchment. 
#2. Compute monthly temp and precipitation and plot the results. 
#3. Compute mean annual precipitation and temperature and plot the results. 
#4. Compute trends in annual precipitation and temperature and plot the results. 

#1 Assignment:

df['(3)T.Max'] = pd.to_numeric(df['(3)T.Max'], errors='coerce') # Convert to numeric
df['(4)T.Min'] = pd.to_numeric(df['(4)T.Min'], errors='coerce')

df['Mean_Temp'] = (df['(3)T.Max'] + df['(4)T.Min']) / 2 
print(df[['(3)T.Max','(4)T.Min','Mean_Temp']].head())


#Subsetting into it respecive month 
df['(2)Date'] = pd.to_datetime(df['(2)Date'], dayfirst=True, errors='coerce')

january_df = df[df['(2)Date'].dt.month == 1]
february_df = df[df['(2)Date'].dt.month == 2]
march_df = df[df['(2)Date'].dt.month == 3]
april_df = df[df['(2)Date'].dt.month == 4]
may_df = df[df['(2)Date'].dt.month == 5]
june_df = df[df['(2)Date'].dt.month == 6]
july_df = df[df['(2)Date'].dt.month == 7]
august_df = df[df['(2)Date'].dt.month == 8]
september_df = df[df['(2)Date'].dt.month == 9]
october_df = df[df['(2)Date'].dt.month == 10]
november_df = df[df['(2)Date'].dt.month == 11]
december_df = df[df['(2)Date'].dt.month == 12]

january_df.iloc[1:].to_csv('January_Temp.csv', index=False)
february_df.iloc[1:].to_csv('February_Temp.csv', index=False)
march_df.iloc[1:].to_csv('March_Temp.csv', index=False)
april_df.iloc[1:].to_csv('April_Temp.csv', index=False)
may_df.iloc[1:].to_csv('May_Temp.csv', index=False)
june_df.iloc[1:].to_csv('June_Temp.csv', index=False)
july_df.iloc[1:].to_csv('July_Temp.csv', index=False)
august_df.iloc[1:].to_csv('August_Temp.csv', index=False)
september_df.iloc[1:].to_csv('September_Temp.csv', index=False)
october_df.iloc[1:].to_csv('October_Temp.csv', index=False)
november_df.iloc[1:].to_csv('November_Temp.csv', index=False)
december_df.iloc[1:].to_csv('December_Temp.csv', index=False)