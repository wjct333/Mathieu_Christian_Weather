import matplotlib.pyplot as plt
import csv
import numpy as np

def plot_weather_precipitation():
    pass

file = open('Weather Data_CSV.csv',"r") # Import data
reader = csv.reader(file)

result = []
rainfall = []
temperature = []
next(reader)
for row in reader:
    if row[4] == '':
        continue
    rainfall.append(float(row[4]))
    temperature.append(float(row[5]))
    result.append(row[2] + '-' + row[3])
print(rainfall)
print(temperature)
print(result)

# ''' Plot barchart '''
fig = plt.figure(figsize=(20,20))
y_pos = np.arange(len(result))
plt.bar(y_pos, rainfall, align='center', alpha=0.5)
plt.xticks(y_pos, result)
plt.ylabel('rainfall')
plt.title('Weather Data')

# ''' Plot linear relationship '''
fig = plt.figure(figsize=(20,20))
plt.plot(result,temperature)  # Plotting graph on rainfall vs year_month
plt.xlabel('Year_Month')
plt.ylabel('Temperature')


plt.show()

file.close()

