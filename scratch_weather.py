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

print(float())