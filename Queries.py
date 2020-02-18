import Functions as Func
import FirstExploring as FE

try:
    # 4.1, time complexity: O(n) n- number of rows
    print("The id's of the max temp received in the data are: ", list(FE.data[FE.data['temp'] == FE.max_temp]['id']))

    # 4.2, time complexity: O(n+m) n- number of rows m-number of columns
    temp_Out = FE.data[Func.get_specific_str_from_col(FE.data, 'out/in', 'Out')]['temp']
    temp_In = FE.data[Func.get_specific_str_from_col(FE.data, 'out/in', 'In')]['temp']
    print(
        'The ratio of temperature between the devices installed outside the room and those installed inside '
        'the room is:', temp_Out.sum() / temp_In.sum())

    # 4.3, time complexity: O(n) n- number of rows
    print('The average temperature of the devices installed inside the room is', temp_In.mean())

    # 4.4, time complexity: O(n) n- number of rows
    print('The average temperature of the devices installed outside the room is', temp_Out.mean())

    # 4.5, time complexity: O(n+m) n- number of rows m-number of columns
    temps, rows = Func.get_num_of_rows_for_elements(FE.data, 'temp')
    print('The number of rows for each temperature:')
    for temp in range(temps.size):
        print('For temperature', temps[temp], '-', rows[temp], 'rows.')

    # 4.6, time complexity: O(n+m) n- number of rows m-number of columns
    print('The temperature values are:', list(Func.get_num_of_groups_in_col(FE.data, 'temp')))

    # 4.7, time complexity: O(n) n- number of rows
    print('The number of rows, where the temperature is between 30 to 37 is:',
          FE.data[(FE.data['temp'] >= 30) & (FE.data['temp'] <= 37)]['temp'].size)

    # 4.8, time complexity: O(n+m) n- number of rows m-number of columns
    print('The first 3 temperatures in the data are:', list(Func.get_top_k_elements(FE.data, 'temp', 3)))

except:
    print('Error while Calculating queries.')

