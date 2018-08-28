import random, datetime

def combSort(data):
    gap = len(data)
    shrink = 1.3
    isSorted = False
    while isSorted is False:
        gap = int(gap / shrink)
        if gap > 1:
            isSorted = False
        else:
            gap = 1
            isSorted = True
        i = 0
        while i + gap < len(data):
            if data[i] > data[i + gap]:
                data[i], data[i + gap] = data[i + gap], data[i]
                isSorted = False
            i += 1
    return data


def perforamnce_combsort(array_size, iterations, range_start, range_end):
    array_size_values = []
    time_values = []
    for num in range(6):
        sorted_array = [0] * (array_size + 1)
        starting_time = datetime.datetime.now()
        for val in range(iterations):
            random_array = [random.randrange(range_start, range_end, 1) for i in range(array_size)]
            combSort(random_array)
        finishing_time = datetime.datetime.now()
        array_size_values.append(array_size)
        time_values.append((finishing_time - starting_time).microseconds)
        print((finishing_time - starting_time).microseconds, " microseconds taken by combsort to sort an array of size ", array_size , "for iterations ", iterations)
        array_size *= 10
    return array_size_values, time_values

#perforamnce_combsort(10,10,0,255)
#perforamnce_combsort(10,10,0,2147483647)
perforamnce_combsort(10,10,0,9223372036854775807)
