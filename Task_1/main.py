import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
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
df['(2)Date'] = pd.to_datetime(df['(2)Date'], dayfirst=True, format='%d/%m/%Y', errors='coerce')

#This is for Question 1 
print("Daily Mean Temperature and Precipitation")
print("--------------------------------------------------") 
daily_mean_temp = []
daily_mean_precipitation = []

for day in range(1, 32):
    day_df = df[df['(2)Date'].dt.day == day]
    day_mean_temp = day_df['Mean_Temp'].astype(float).mean()
    day_mean_precipitation = day_df['(5)Rain'].astype(float).mean()
    print(f"Day: {day}, Mean Temp: {day_mean_temp:.2f}, Precipitation: {day_mean_precipitation:.2f}")

    daily_mean_temp.append(day_mean_temp)
    daily_mean_precipitation.append(day_mean_precipitation)

plt.figure(figsize=(10, 6))
plt.plot(range(1,32), daily_mean_precipitation, marker ='o', label='Daily Mean Precipitation', color='blue', alpha=0.6)
plt.xlabel('Day of Month')
plt.ylabel('Daily Mean Precipitation (mm)')
plt.title('Daily Mean Percipitation over a Decade')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(range(1,32), daily_mean_temp, marker='s', label='Daily Mean Temperature', color='red', alpha=0.6)
plt.xlabel('Day of Month')
plt.ylabel('Daily Mean Temperature (°C)')
plt.title('Daily Mean Temperature over a Decade')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


print()

#This is for Question 2
monthly_mean_temp = []
monthly_mean_precipitation = []
print("Monthly Mean Temperature and Precipitation")
print("--------------------------------------------------")
for month in range(1, 13):
    month_df = df[df['(2)Date'].dt.month == month]
    month_mean_temp = month_df['Mean_Temp'].astype(float).mean()
    month_mean_precipitation = month_df['(5)Rain'].astype(float).mean()
    print(f"Month: {month}, Mean Temp: {month_mean_temp:.2f}, Precipitation: {month_mean_precipitation:.2f}")

    monthly_mean_temp.append(month_mean_temp)
    monthly_mean_precipitation.append(month_mean_precipitation)

plt.figure(figsize=(10, 6))
plt.plot(range(1,13), monthly_mean_precipitation,marker ='o',  label='Monthly Mean Precipitation', color='blue', alpha=0.6)
plt.xlabel('Month of a Year')
plt.ylabel('Monthly Mean Precipitation (mm)')
plt.title('Monthly Mean Precipitation over a Decade')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(range(1,13), monthly_mean_temp,marker='s',  label='Monthly Mean Temperature', color='red', alpha=0.6)
plt.xlabel('Month of a Year')
plt.ylabel('Monthly Mean Temperature (°C)')
plt.title('Monthly Mean Temperature over a Decade')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print()

print("Annual Mean Temperature and Precipitation")
print("--------------------------------------------------")
yearly_mean_temp = []
yearly_mean_precipitation = []

for year in range(1985, 1996):
    year_df = df[df['(2)Date'].dt.year == year]
    year_mean_temp = year_df['Mean_Temp'].astype(float).mean()
    year_mean_precipitation = year_df['(5)Rain'].astype(float).mean()
    print(f"Year: {year}, Mean Temp: {year_mean_temp:.2f}, Precipitation: {year_mean_precipitation:.2f}")

    yearly_mean_temp.append(year_mean_temp)
    yearly_mean_precipitation.append(year_mean_precipitation)

#This if for Question 3
plt.figure(figsize=(10, 6))
plt.plot(range(1985,1996), yearly_mean_precipitation, marker ='o',  label='Yearly Mean Precipitation', color='blue', alpha=0.6)
plt.xlabel('Year')
plt.ylabel('Annual Mean Precipitation (mm)')
plt.title('Annual Mean Precipitation over a Decade')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(range(1985,1996), yearly_mean_temp, marker='s',  label='Yearly Mean Temp Per Year', color='red', alpha=0.6)
plt.xlabel('Year')
plt.ylabel('Annual Mean Temperature (°C)')
plt.title('Annual Mean Temperature over a Decade')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

#This is for Question 4 
yearly_precipitation = []
yearly_mean_temp = []
for year in range(1985, 1996):
    year_df = df[df['(2)Date'].dt.year == year]
    year_mean_temp = year_df['Mean_Temp'].astype(float).mean()
    year_precipitation = year_df['(5)Rain'].astype(float).mean()
    
    yearly_mean_temp.append(year_mean_temp)
    yearly_precipitation.append(year_precipitation)

x= list(range(1985, 1996))
y=yearly_precipitation
slope, intercept = np.polyfit(x, y, 1)
predicted_y = slope * np.array(x) + intercept
plt.figure(figsize=(10, 6))
plt.plot(x, y,marker='o',  label='Annual Mean Precipitation', color='red', alpha=0.6)
plt.plot(x, predicted_y, color='blue', label='Trend Line', linewidth=1)
plt.xlabel('Year')
plt.ylabel('Annual Mean Precipitation (mm)')
plt.title('Mean Precipitation/Year Trend Plot')
r2_value = r2_score(y, predicted_y)
ax = plt.gca()
ax.text(0.05,0.95, f'Equation: y = {slope:.2f}x + {intercept:.2f}, R2 value is: {r2_value:.4f}',transform=ax.transAxes,  fontsize=12, color='blue')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()



x= list(range(1985, 1996))
y=yearly_mean_temp
slope, intercept = np.polyfit(x, y, 1)
predicted_y = slope * np.array(x) + intercept
plt.figure(figsize=(10, 6))
plt.plot(x, y,marker='s',  label='Annual Mean Temp', color='red', alpha=0.6)
plt.plot(x, predicted_y, color='blue', label='Trend Line', linewidth=1)
plt.xlabel('Year')
plt.ylabel('Annual Mean Temperature (°C)')
plt.title('Mean Temperature/Year Trend Plot')
r2_value = r2_score(y, predicted_y)
ax = plt.gca()
ax.text(0.05,0.95, f'Equation: y = {slope:.2f}x + {intercept:.2f}, R2 value is: {r2_value:.4f}',transform=ax.transAxes,  fontsize=12, color='blue')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()