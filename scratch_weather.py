# def pri()
#     print()
# return pri

import matplotlib.pyplot as plt

years = [2014,2015,2016,2017,2018]

months = ["Jan", "Feb"]

rainfall = [11, 22, 31, 12, 43, 26, 42, 12, 24, 23]

# def plot_weather_rainfall:
year_month = []
for year in years:
    for month in months:
        # year_month = years.append(month)
        label = '-'.join([str(year),month])
        year_month.append(label)
print (year_month)

plt.plot(year_month, rainfall)
plt.ylabel('month')
plt.show()

# def plot_weather_temperature:

# # print(''.join(month))
#
# # number_string = []
# # number_string.append(1)
# # number_string.append(1)
# # print(number_string)
#
# result = Jan-2010

# print(str(2010)+"B")
