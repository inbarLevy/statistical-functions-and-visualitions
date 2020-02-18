import numpy as np
from scipy import stats
from FirstExploring import mean_temp, std_temp, data


# 3.1, time complexity: O(n+m) n- number of rows m-number of columns
def calc_average(data_frame, col_name):
    if col_name not in data_frame.columns:
        print('Column was not found.')
        return
    elif np.size(data_frame[col_name]) == 0:
        print('Dataframe is empty.')
        return
    else:
        return np.sum(data_frame[col_name]) / np.size(data_frame[col_name])


# 3.2, time complexity: O(n+m) n- number of rows m-number of columns
def calc_std(data_frame, col_name):
    if col_name not in data_frame.columns:
        print('Column was not found.')
        return
    elif np.size(data_frame[col_name]) == 0:
        print('Dataframe is empty.')
        return
    else:
        temp = data_frame[col_name] - calc_average(data_frame, col_name)
        return np.sqrt(np.sum(temp ** 2) / (np.size(data_frame[col_name]) - 1))


# 3.3, time complexity: O(n+m) n- number of rows m-number of columns
def calc_variance(data_frame, col_name):
    if col_name not in data_frame.columns:
        print('Column was not found.')
        return
    elif np.size(data_frame[col_name]) == 0:
        print('Dataframe is empty.')
        return
    else:
        return calc_std(data_frame, col_name) ** 2


# 3.4, time complexity: O(n+m) n- number of rows m-number of columns
def calc_mode(data_frame, col_name):
    if col_name not in data_frame.columns:
        print('Column was not found.')
        return
    elif np.size(data_frame[col_name]) == 0:
        print('Dataframe is empty.')
        return
    else:
        return int(stats.mode(data_frame[col_name])[0])


# Verification:
# time complexity for the first two prints: O(1), time complexity for the last two prints O(n) n- number of rows

print('Verification:')
print('pandas', mean_temp, 'VS. function:', calc_average(data, 'temp'))
print('pandas', std_temp, 'VS. function:', calc_std(data, 'temp'))
print('pandas', data['temp'].var(), 'VS. function:', calc_variance(data, 'temp'))
print('pandas', data['temp'].mode()[0], 'VS. function:', calc_mode(data, 'temp'))

