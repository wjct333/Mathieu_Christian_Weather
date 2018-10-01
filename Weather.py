import matplotlib.pyplot as plt
import csv
import numpy as np

def plot_weather_precipitation():
    pass

file = open('Weather Data_CSV.csv',"r") # Importing weather data
reader = csv.reader(file)

result = []                # Extracting and combining year and month data
rainfall = []
next(reader)
for row in reader:
    if row[4] == '':
        continue
    rainfall.append((row[4]))
    result.append(row[2] + '-' + row[3])
rainfall = rainfall[1:-1]
result = result[1:-1]
print(rainfall)
print(result)
#
# ''' Plot linear relationship '''
fig = plt.figure(figsize=(20,20))
plt.plot(result,rainfall)  # Plotting graph on rainfall vs year_month
plt.xlabel('Year_Month')
plt.ylabel('rainfall')
#
# ''' Plot barchart '''
y_pos = np.arange(len(result))
plt.bar(y_pos, rainfall, align='center', alpha=0.5)
plt.xticks(y_pos, result)
plt.ylabel('rainfall')
plt.title('Weather Data')

plt.show()

file.close()

