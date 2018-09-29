# Importing weather data

import matplotlib.pyplot as plt
import csv

file = open('Data/Rainfall Data.csv',"r")

reader = csv.reader(file)         # Alls to create list

print(reader)

for row in reader:

    years = row[2]
    months = row[3]
    rainfall = row[4]
    # print(list(int(years)))
    year_month = []
    for year in years:
        for month in months:
            year_month = years.append(months)
            labelled = '-'.join([str(year),month])
            year_month.append(labelled)
    print(year_month)

# plt.plot(year_month, rainfall)
# plt.ylabel('month')
# plt.show()

# file.close()

