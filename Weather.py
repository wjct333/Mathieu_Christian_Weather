import matplotlib.pyplot as plt
import csv
import numpy as np

def plot_weather_precipitation():
    pass

file = open('Weather Data_CSV.csv',"r") # Importing weather data
reader = csv.reader(file)

result = []                # Extracting and combining year and month data
rainfall = []
for row in reader:
    rainfall.append((row[4]))
    result.append(row[2] + '-' + row[3])
print(result, rainfall)

fig = plt.figure(figsize=(20,20))
plt.plot(result,rainfall)  # Plotting graph on rainfall vs year_month
plt.xlabel('Year_Month')
plt.ylabel('rainfall')

plt.show()

file.close()

