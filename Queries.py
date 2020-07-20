import Functions as Func
import FirstExploring as FE

try:
    # What is the id of the top (max) temp received in our data? 
    print("The id's of the max temp received in the data are: ", list(FE.data[FE.data['temp'] == FE.max_temp]['id']))

    # What is the ratio between temperatures were measured outside to temperatures were measured inside?  
    temp_Out = FE.data[Func.get_specific_str_from_col(FE.data, 'out/in', 'Out')]['temp']
    temp_In = FE.data[Func.get_specific_str_from_col(FE.data, 'out/in', 'In')]['temp']
    print(
        'The ratio of temperature between the devices installed outside the room and those installed inside '
        'the room is:', temp_Out.sum() / temp_In.sum())

    # What is the average of inside temperature? (measured inside) 
    print('The average temperature of the devices installed inside the room is', temp_In.mean())

    # What is the average of outside temperature? (measured outside) 
    print('The average temperature of the devices installed outside the room is', temp_Out.mean())

    # How many data were collected according to each temperature?
    temps, rows = Func.get_num_of_rows_for_elements(FE.data, 'temp')
    print('The number of rows for each temperature:')
    for temp in range(temps.size):
        print('For temperature', temps[temp], '-', rows[temp], 'rows.')

    #  Find the list which contains all temperature values. (without duplicates) 
    print('The temperature values are:', list(Func.get_num_of_groups_in_col(FE.data, 'temp')))

    # How many rows exist where the temperature between 30 to 37? 
    print('The number of rows, where the temperature is between 30 to 37 is:',
          FE.data[(FE.data['temp'] >= 30) & (FE.data['temp'] <= 37)]['temp'].size)

    #  What is the top 3 temperatures? (​By their appearance in the data) 
    print('The first 3 temperatures in the data are:', list(Func.get_top_k_elements(FE.data, 'temp', 3)))

except:
    print('Error while Calculating queries.')

