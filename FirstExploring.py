import pandas as pd

try:
    # 2.1, time complexity: O(n*m) n- number rows m-number of columns.
    data = pd.read_csv('IOT-temp.csv')
    num_of_rows, num_of_cols = data.shape
except:
    print('Error while handling file.')

try:
    if __name__ == '__main__':
        # 2.2, time complexity: O(1)
        print('Rows: ', num_of_rows, 'Cols: ', num_of_cols)

        # 2.3, time complexity: O(n) n- number of columns
        print(' Columns names: ', list(data.columns))

    # 2.4, time complexity for each one: O(n) n- number of rows
    max_temp = data['temp'].max()
    min_temp = data['temp'].min()
    mean_temp = data['temp'].mean()
    median_temp = data['temp'].median()
    std_temp = data['temp'].std()
    count_temp = data['temp'].count()
    sum_temp = data['temp'].sum()

    if __name__ == '__main__':
        # 2.5, time complexity: O(1)
        print('The range of temperature values is', max_temp - min_temp)

        # 2.6 , time complexity for each one: O(1)
        print('Statements:')
        print('The maximum temperature measured is', max_temp)
        print('The minimum temperature measured is', min_temp)
        print('The average temperature measured is', mean_temp)
        print('The median temperature measured is', median_temp)
        print('The standard deviation of the temperature is', std_temp)
        print('The amount of temperatures measured is', count_temp)
        print('The sum of the measured temperatures is', sum_temp)

except:
    print('Error while Calculating the statistics.')


