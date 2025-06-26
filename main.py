import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import calendar

df = pd.read_csv('./Data/Input_Climate.csv')

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

#Data Formatting:
df['(3)T.Max'] = pd.to_numeric(df['(3)T.Max'], errors='coerce') # Convert to numeric
df['(4)T.Min'] = pd.to_numeric(df['(4)T.Min'], errors='coerce')
df['(5)Rain'] = pd.to_numeric(df['(5)Rain'], errors='coerce') # Convert to numeric

df['Mean_Temp'] = (df['(3)T.Max'] + df['(4)T.Min']) / 2 
df['(2)Date'] = pd.to_datetime(df['(2)Date'], dayfirst=True, errors='coerce')

print("Daily Mean Temperature and Precipitation")
print("--------------------------------------------------") 
daily_mean_temp = []
daily_precipitation = []

for day in range(1, 32):
    day_df = df[df['(2)Date'].dt.day == day]
    day_mean_temp = day_df['Mean_Temp'].astype(float).mean()
    day_precipitation = day_df['(5)Rain'].astype(float).sum()
    print(f"Day: {day}, Mean Temp: {day_mean_temp:.2f}, Precipitation: {day_precipitation:.2f}")

    daily_mean_temp.append(day_mean_temp)
    daily_precipitation.append(day_precipitation)

plt.figure(figsize=(10, 6))
plt.scatter(daily_mean_temp, daily_precipitation, label='Daily Mean Temp / Daily Precipitation', color='blue', alpha=0.6)

plt.xlabel('Daily Temperature Mean (°C)')
plt.ylabel('Daily Precipitation (mm)')
plt.title('Daily Temperature Mean and Precipitation')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


print()


monthly_mean_temp = []
monthly_precipitation = []

print("Monthly Mean Temperature and Precipitation")
print("--------------------------------------------------")
for month in range(1, 13):
    month_df = df[df['(2)Date'].dt.month == month]
    month_mean_temp = month_df['Mean_Temp'].astype(float).mean()
    month_precipitation = month_df['(5)Rain'].astype(float).sum()
    print(f"Month: {month}, Mean Temp: {month_mean_temp:.2f}, Precipitation: {month_precipitation:.2f}")

    monthly_mean_temp.append(month_mean_temp)
    monthly_precipitation.append(month_precipitation)

plt.figure(figsize=(10, 6))
plt.scatter(monthly_mean_temp, monthly_precipitation, label='Monthly Mean Temp / Monthly Precipitation', color='blue', alpha=0.6)

plt.xlabel('Monthly Temperature Mean (°C)')
plt.ylabel('Monthly Precipitation (mm)')
plt.title('Monthly Temperature Mean and Precipitation')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print()


print("Yearly Mean Temperature and Precipitation")
print("--------------------------------------------------")
yearly_mean_temp = []
yearly_precipitation = []

for year in range(1985, 1996):
    year_df = df[df['(2)Date'].dt.year == year]
    year_mean_temp = year_df['Mean_Temp'].astype(float).mean()
    year_precipitation = year_df['(5)Rain'].astype(float).sum()
    print(f"Year: {year}, Mean Temp: {year_mean_temp:.2f}, Precipitation: {year_precipitation:.2f}")

    yearly_mean_temp.append(year_mean_temp)
    yearly_precipitation.append(year_precipitation)

plt.figure(figsize=(10, 6))
plt.scatter(yearly_mean_temp, yearly_precipitation, label='Yearly Mean Temp / Yearly Precipitation', color='blue', alpha=0.6)

plt.xlabel('Yearly Temperature Mean (°C)')
plt.ylabel('Yearly Precipitation (mm)')
plt.title('Yearly Temperature Mean and Precipitation')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
