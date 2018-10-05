import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd


# def load_Weather():
#     pass
#
# def plot_weather_precipitation():
#
#
#     file = open('Weather Data_CSV.csv',"r") # Import data
#     reader = csv.reader(file)
#
#     result = []
#     rainfall = []
#     temperature = []
#     next(reader)
#     for row in reader:
#         if row[4] == '':
#             continue
#         rainfall.append(float(row[4]))
#         temperature.append(float(row[5]))
#         result.append(row[2] + '-' + row[3])
#     print(rainfall)
#     print(temperature)
#     print(result)
#
#     fig = plt.figure(figsize=(20,20))
#     ax = fig.add_subplot(111)
#
#     # ''' Plot barchart '''
#     y_pos = np.arange(len(result))                      # x-axis - time
#     ax.bar(y_pos, rainfall, align='center', alpha=0.5)
#     plt.xticks(y_pos, result)
#     plt.ylabel('rainfall')
#     plt.title('Weather Data')
#     fig.autofmt_xdate()
#
#     # ''' Plot linear relationship '''
#     ax2 = ax.twinx()
#     ax2.plot(result,temperature)  # Plotting graph on rainfall vs year_month
#     plt.xlabel('Year_Month')
#     plt.ylabel('Temperature')
#
#     plt.show()
#
#     file.close()

# plot_weather_precipitation()
#
# file = open('Weather Data_CSV.csv', "r")  # Import data
# reader = csv.reader(file)
#
# df = pd.read_csv('Weather Data_CSV.csv')
# df['year'] = pd.to_datetime(df['year'])
# df['quarter'] = df.result.dt.quarter
#
# df.groupby(['quarter'])['rainfall'].mean()


def plot_rainfall():
    print(
        '\n\nThe price and production correlation cacualtion showed there was a strong correation between the price and production for the three selected variities.\nThe price and prouction charts shows the highest price and production for all four selected varities in 2017 and a reduction for \nboth production and price in 2018. Hence we will analysis the claimate for the 2016 and 2017 to find if there was any \nweather change effect the production qulity in 2017 and 2018.\n')

    # comparing  the annual rainfall for the comparative years and display
    plt.xlabel('Year')
    plt.ylabel('Total Rainfall (millimetres)')
    plt.title('Annual Total Rainfall 2013-2017')
    rainfalls_by_years = []
    result = []
    rainfall = []
    temperature = []
    file = open('Weather Data_CSV.csv',"r") # Import data
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row[4] == '':
            continue
        rainfall.append(float(row[4]))
        temperature.append(float(row[5]))
        result.append(row[2] + '-' + row[3])
    # calculating the total annual rainfall
    for i in range(5):
        sum = 0
        for month in range(12):
            sum += rainfall[i]
        rainfalls_by_years.append(sum)
    plt.bar(range(5), rainfalls_by_years)
    plt.grid()
    plt.show()

plot_rainfall()