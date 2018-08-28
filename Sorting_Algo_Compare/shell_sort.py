import random, datetime
def shellSort(data):
    gap = len(data) // 2
    while gap > 0:
        for startposition in range(gap):
            gapInsertionSort(data, startposition, gap)
        gap = gap // 2


def gapInsertionSort(data, start, gap):
    for i in range(start + gap, len(data), gap):

        currentvalue = data[i]
        position = i

        while position >= gap and data[position - gap] > currentvalue:
            data[position] = data[position - gap]
            position = position - gap

        data[position] = currentvalue



def perforamnce_shell(array_size, iterations, range_start, range_end):
    array_size_values = []
    time_values = []
    for num in range(6):
        sorted_array = [0] * (array_size + 1)
        starting_time = datetime.datetime.now()
        for val in range(iterations):
            random_array = [random.randrange(range_start, range_end, 1) for i in range(array_size)]
            shellSort(random_array)
        finishing_time = datetime.datetime.now()
        array_size_values.append(array_size)
        time_values.append((finishing_time - starting_time).microseconds)
        print((finishing_time - starting_time).microseconds, " microseconds taken by  shell sort to sort an array of size ", array_size , "for iterations ", iterations)
        array_size *= 10
    return array_size_values, time_values

#perforamnce_shell(10,10,0,255)
#perforamnce_shell(10,10,0,2147483647)
perforamnce_shell(10,10,0,9223372036854775807)