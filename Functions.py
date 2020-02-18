# time complexity: O(n+m) n- number of rows m-number of columns
def get_specific_str_from_col(data_frame, col_name, str):
    if col_name not in data_frame.columns:
        print('Column was not found.')
        return
    elif data_frame[col_name].size == 0:
        print('Dataframe is empty.')
        return
    elif str not in data_frame[col_name].values:
        print(str, 'was not found.')
        return
    else:
        return data_frame[col_name].str.contains(str, na=False)


# time complexity: O(n+m) n- number of rows m-number of columns
def get_num_of_rows_for_elements(data_frame, col_name):
    if col_name not in data_frame.columns:
        print('Column was not found.')
        return
    elif data_frame[col_name].size == 0:
        print('Dataframe is empty.')
        return
    else:
        return data_frame[col_name].value_counts().index, data_frame[col_name].value_counts().values


# time complexity: O(n+m) n- number of rows m-number of columns
def get_num_of_groups_in_col(data_frame, col_name):
    if col_name not in data_frame.columns:
        print('Column was not found.')
        return
    elif data_frame[col_name].size == 0:
        print('Dataframe is empty.')
        return
    else:
        return data_frame[col_name].drop_duplicates()


# time complexity: O(n+m) n- number of rows m-number of columns
def get_top_k_elements(data_frame, col_name, k):
    if col_name not in data_frame.columns:
        print('Column was not found.')
        return
    elif data_frame[col_name].size == 0:
        print('Dataframe is empty.')
        return
    elif type(k) != int:
        print('incorrect value.')
        return
    else:
        return data_frame[col_name].head(k)


# time complexity: O(n) n- number of rows
def get_temp_OutIn_ratio(data_frame):
    tot_temp = data_frame['temp'].size
    if tot_temp == 0:
        print('Dataframe is empty.')
        return
    else:
        temp_Out = data_frame[get_specific_str_from_col(data_frame, 'out/in', 'Out')]['temp'].count() / tot_temp
        temp_In = data_frame[get_specific_str_from_col(data_frame, 'out/in', 'In')]['temp'].count() / tot_temp
        return [round(temp_Out * 100, 2), round(temp_In * 100, 2)]


# time complexity: O(n) n- number of rows
def get_tempsValues_and_tempsMean(data_frame, string):
    if data_frame['temp'].size == 0:
        print('Dataframe is empty.')
        return
    if string not in ['In', 'Out']:
        print(string, 'was not found.')
        return
    else:
        temp_mean = data_frame[get_specific_str_from_col(data_frame, 'out/in', string)]['temp'].mean()
        temps = data_frame[get_specific_str_from_col(data_frame, 'out/in', string)]['temp'].drop_duplicates().values
        return temps, temp_mean
