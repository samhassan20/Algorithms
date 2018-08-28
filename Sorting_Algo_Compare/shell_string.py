import datetime, random

input_words = []
with open("words.txt") as f:
    lines = f.readlines()
    for val in lines:
        input_words.append(val)

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



def perforamnce_shell_sort(array_size, iterations, input_data):
    array_size_values = []
    time_values = []
    for num in range(6):
        starting_time = datetime.datetime.now()
        for val in range(iterations):
            random_array = [input_words[random.randint(0,len(input_data)-1)] for i in range(array_size)]
            shellSort(random_array)
        finishing_time = datetime.datetime.now()
        array_size_values.append(array_size)
        time_values.append((finishing_time - starting_time).microseconds)
        print((finishing_time - starting_time).microseconds, " microseconds taken by shell sort to sort an array of size ", array_size , "for iterations ", iterations)
        array_size *= 10
    return array_size_values, time_values

perforamnce_shell_sort(10,10,input_words)