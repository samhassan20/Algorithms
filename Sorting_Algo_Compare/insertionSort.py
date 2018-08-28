import random, datetime
def insertion(data):
    for i in range(0, len(data)):
        tmp = data[i]
        j = i - 1
        while (j > -1 and data[j] > tmp):
            data[j + 1] = data[j]
            j = j - 1
            data[j + 1] = tmp
    return data


def perforamnce_insertionsort(array_size, iterations, range_start, range_end):
    array_size_values = []
    time_values = []
    for num in range(6):
        sorted_array = [0] * (array_size + 1)
        starting_time = datetime.datetime.now()
        for val in range(iterations):
            random_array = [random.randrange(range_start, range_end, 1) for i in range(array_size)]
            insertion(random_array)
        finishing_time = datetime.datetime.now()
        array_size_values.append(array_size)
        time_values.append((finishing_time - starting_time).microseconds)
        print((finishing_time - starting_time).microseconds, " microseconds taken by selection sort to sort an array of size ", array_size , "for iterations ", iterations)
        array_size *= 10
    return array_size_values, time_values

#perforamnce_insertionsort(10,10,0,255)
#perforamnce_insertionsort(10,10,0,2147483647)
perforamnce_insertionsort(10,10,0,9223372036854775807)
