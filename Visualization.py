import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import Functions as func
import FirstExploring as EF

# visualization for query number 2: What is the ratio between temperatures were measured outside to temperatures  were measured inside
temps = func.get_temp_OutIn_ratio(EF.data)
labels = ['Out', 'In']
plt.pie(temps, labels=labels, colors=('darkcyan', 'darkblue'), autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('The ratio of temperature between the devices installed outside and inside the room')
plt.show()

# visualization for query number 3: What is the average of inside temperature?
temps, mean = func.get_tempsValues_and_tempsMean(EF.data, 'In')
mean = [mean] * temps.size
x = np.arange(0, temps.size)
fig, ax = plt.subplots()
ax.scatter(x, temps, label='temperature', color='navy')
ax.plot(x, mean, label='Mean', linestyle='--', color='olive')
plt.xticks(x)
plt.yticks(np.arange(temps.min(), temps.max()))
plt.xlabel('index')
plt.ylabel('temperature')
plt.title('Inside temperatures and their average')
legend = ax.legend(loc='best')
plt.show()

# visualization for query number 4: What is the average of outside temperature?
temps, mean = func.get_tempsValues_and_tempsMean(EF.data, 'Out')
mean = [mean] * temps.size
x = np.arange(0, temps.size)
fig, ax = plt.subplots()
data_line = ax.scatter(x, temps, label='temperature', color='purple')
mean_line = ax.plot(x, mean, label='Mean', linestyle='--', color='darkorange')
plt.xticks(x)
plt.yticks(np.arange(temps.min(), temps.max()))
plt.xlabel('index')
plt.ylabel('temperature')
plt.title('Outside temperatures and their average')
legend = ax.legend(loc='best')
plt.show()

# visualization for query number 5: How many data were collected according to each temperature?
temps, rows = func.get_num_of_rows_for_elements(EF.data, 'temp')
plt.ylabel('number of rows')
plt.xlabel('temperature')
plt.title('Number of rows for each temperature')
colors = np.random.rand(temps.size)
plt.xticks(temps)
plt.bar(temps, rows)
plt.show()

# visualization for query number 8: What is the top 3 temperatures?
locations = ['0', '1', '2']
temps = func.get_top_k_elements(EF.data, 'temp', 3)
plt.yticks(temps)
plt.xlabel('Location in the data')
plt.ylabel('temperature')
plt.title('Top 3 temperatures')
plt.bar(locations, temps, color='lightpink', edgecolor='darkred', linewidth=0.5, width=0.3)
plt.show()

# Conclusions:
x = ['max', 'min', 'range', 'average', 'median', 'std']
temp = [EF.max_temp, EF.min_temp, EF.max_temp - EF.min_temp, EF.mean_temp, EF.median_temp, EF.std_temp]
plt.xlabel('statistics values')
plt.ylabel('temperature')
plt.yticks(temp)
plt.title('statistical Conclusions')
plt.bar(x, temp, color='darkgrey', edgecolor='slategrey', linewidth=1, width=0.5)
plt.show()

pd.DataFrame.hist(data=EF.data, column='temp', grid=True)
plt.xlabel('temperature')
plt.ylabel('frequencies')
plt.title('histogram for the temperatures')
plt.show()
