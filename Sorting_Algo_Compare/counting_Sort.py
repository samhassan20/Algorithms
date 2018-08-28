import datetime,random
import numpy as np

def my_countsort(array_1,array_2, num_range):
    #Putting all zeros in array_3
    array_3 = [0] * (max(array_1)+1)
    #putting count of values of A in indexes of C.
    for i in array_1:
        array_3[i] +=1
    #Replacing count with cumulative sum
    array_3 = np.cumsum(array_3)
    #Putting values from array_3 to array_2 and decrementing particular cumulative sum value by 1.
    for j in range(len(array_1),0,-1):
        array_2[array_3[array_1[j-1]]] = array_1[j-1]
        array_3[array_1[j-1]] = array_3[array_1[j-1]] - 1
    return array_2[1:]

def perforamnce_countsort(array_size, iterations, range_start, range_end):
    array_size_values = []
    time_values = []
    for num in range(5):
        sorted_array = [0] * (array_size + 1)
        starting_time = datetime.datetime.now()
        for val in range(iterations):
            random_array = [random.randrange(range_start, range_end, 1) for i in range(array_size)]
            my_countsort(random_array,sorted_array, range_end-range_start)
        finishing_time = datetime.datetime.now()
        array_size_values.append(array_size)
        time_values.append((finishing_time - starting_time).microseconds)
        print((finishing_time - starting_time).microseconds, " microseconds taken by countsort to sort an array of size ", array_size , "for iterations ", iterations)
        array_size *= 10
    return array_size_values, time_values

CS_Array_Size_8,CS_time_8 =perforamnce_countsort(10,100,0,255)