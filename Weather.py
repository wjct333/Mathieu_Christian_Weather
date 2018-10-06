import matplotlib.pyplot as plt
import csv
import numpy as np


def load_Weather():
    pass

def plot_weather_precipitation():

    file = open('Weather Data_CSV.csv',"r") # Import data
    reader = csv.reader(file)

    result = []
    rainfall = []
    mean_max_temperature = []
    mean_min_temperature = []
    quarterly_rain = []
    quarterly_min_temp = []
    quarterly_max_temp = []
    quarter = ['2013-Q1', '2013-Q2', '2013-Q3', '2013-Q4', '2014-Q1', '2014-Q2', '2014-Q3', '2014-Q4', '2015-Q1', '2015-Q2', '2015-Q3', '2015-Q4', '2016-Q1', '2016-Q2', '2016-Q3', '2016-Q4', '2017-Q1', '2017-Q2', '2017-Q3', '2017-Q4', '2018-Q1', '2018-Q2']
    next(reader)
    for row in reader:
        if row[4] == '':
            continue
        # else:
        rainfall.append(float(row[4]))
        mean_max_temperature.append(float(row[5]))
        mean_min_temperature.append(float(row[7]))
        result.append(row[2] + '-' + row[3])

    for i in range(0, len(rainfall)-2, 3):
        first_month_rain = rainfall[i]
        second_month_rain = rainfall[i+1]
        third_month_rain = rainfall[i+2]
        sum_month_rain = first_month_rain + second_month_rain + third_month_rain
        quarterly_rain.append(sum_month_rain)

    for i in range(0, len(mean_max_temperature)-2, 3):
        first_month_temp = mean_max_temperature[i]
        second_month_temp = mean_max_temperature[i+1]
        third_month_temp = mean_max_temperature[i+2]
        mean_max_temp = (first_month_temp + second_month_temp + third_month_temp)/3
        quarterly_min_temp.append(mean_max_temp)

    for i in range(0, len(mean_min_temperature)-2, 3):
        first_month_temp = mean_min_temperature[i]
        second_month_temp = mean_min_temperature[i+1]
        third_month_temp = mean_min_temperature[i+2]
        mean_min_temp = (first_month_temp + second_month_temp + third_month_temp)/3
        quarterly_max_temp.append(mean_min_temp)

    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111)

    # ''' Plot barchart '''
    y_pos = np.arange(len(quarter))
    plt.bar(y_pos, quarterly_rain, label='rainfall', align='center', alpha=0.6,edgecolor='black')
    plt.xticks(y_pos, quarter)
    plt.ylabel('Rainfall (mm)')
    plt.title('Weather Data')
    fig.autofmt_xdate()

    # ''' Plot linear relationship '''
    ax2 = ax.twinx()
    ax2.plot(quarter, quarterly_max_temp,label = 'Mean Max Temperature')  # Plotting graph on temperature vs year_month
    ax2.plot(quarter, quarterly_min_temp,label = 'Mean Min Temperature')  # Plotting graph on temperature vs year_month
    ax2.set_ylim([0,35])
    plt.xlabel('Year_Month')
    plt.ylabel('Temperature (°C)')
    plt.grid()
    plt.legend()
    plt.show()

    print(quarterly_rain)
    print(quarterly_max_temp)
    print(quarterly_min_temp)

    file.close()

plot_weather_precipitation()
