import pandas as pd

try:
    data = pd.read_csv('IOT-temp.csv')
    num_of_rows, num_of_cols = data.shape
except:
    print('Error while handling file.')

try:
    if __name__ == '__main__':
        print('number of rows: ', num_of_rows, ', number of columns: ', num_of_cols)

        print(' Columns names: ', list(data.columns))

    max_temp = data['temp'].max()
    min_temp = data['temp'].min()
    mean_temp = data['temp'].mean()
    median_temp = data['temp'].median()
    std_temp = data['temp'].std()
    count_temp = data['temp'].count()
    sum_temp = data['temp'].sum()

    if __name__ == '__main__':
        print('The range of temperature values is', max_temp - min_temp)

        print('Statements:')
        print('The maximum temperature measured is', max_temp)
        print('The minimum temperature measured is', min_temp)
        print('The average temperature measured is', mean_temp)
        print('The median temperature measured is', median_temp)
        print('The standard deviation of the temperature is', std_temp)
        print('The amount of temperatures measured is', count_temp)
        print('The sum of the measured temperatures is', sum_temp)
        print('The range of temperature values is', max_temp-min_temp)

except:
    print('Error while Calculating the statistics.')


