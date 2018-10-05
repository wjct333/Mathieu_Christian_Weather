# import matplotlib.pyplot as plt
#
# years = [2014,2015,2016,2017,2018]
#
# months = ["Jan", "Feb"]
#
# rainfalls = [11, 22, 31, 12, 43, 26, 42, 12, 24, 23]
#
# def plot_weather_precipitation():
#     pass
# year_month = []                # Extracting and combining year and month data
# precipitation = []
# for year in years:
#     for month in months:
#         year_month.append(str(year) + '-' + month)
#
# for rainfall in rainfalls:
#     precipitation.append(rainfall)
# print (year_month, precipitation)
#
# plt.plot(year_month, precipitation)
# plt.xlabel('Year_Month')
# plt.ylabel('Precipitation')
# plt.show()



# Method 1 of opening CSV file:
# file = open('Weather Data_CSV.csv',"r")
# reader = csv.reader(file)         # Alls to create list
# print(reader(0))

# Method 2 of opening CSV file:
# with open('Weather Data_CSV.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')

# Error message:
# Matplotlib: ValueError: x and y must have same first dimension

# a = ('1','2','3','4','5','6')

import matplotlib.pyplot as plt
import csv
import numpy as np


# def plot_weather_data():
file = open('Weather Data_CSV.csv', "r")  # Importing weather data
reader = csv.reader(file)

time = []
rainfall = []
temperature = []
next(reader)                    # ignore the title line
for row in reader:
    if row[4] == '':
            continue            # continue program without crashing on empty string
    rainfall.append(float(row[4]))
    temperature.append(float(row[5]))
    time.append(row[2] + '-' + row[3])    # combining year and month data
print(rainfall)
print(temperature)
print(time)

fig = plt.figure(figsize=(20, 20))
ax = fig.add_subplot(111)

# Plot barchart on rainfall vs time
y_pos = np.arange(len(time))  # x-axis - time
ax.bar(y_pos, rainfall, align='center', alpha=0.5)
plt.xticks(y_pos, time)
plt.ylabel('rainfall')
plt.title('Weather Data')
fig.autofmt_xdate()           # formatting x-axis labels to avoid overlapping

# Plot line graph on temperature vs time
ax2 = ax.twinx()
ax2.plot(time, temperature)  # Plotting graph on temperature vs time
plt.xlabel('Year_Month')
plt.ylabel('Temperature')

plt.show()


file.close()
