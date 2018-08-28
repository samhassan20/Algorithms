import datetime, random

input_words = []
with open("words.txt") as f:
    lines = f.readlines()
    for val in lines:
        input_words.append(val)

def insertion_string(data):
    for i in range(0, len(data)):
        tmp = data[i]
        j = i - 1
        while (j > -1 and data[j] > tmp):
            data[j + 1] = data[j]
            j = j - 1
            data[j + 1] = tmp
    return data


def perforamnce_insertionsort(array_size, iterations, input_data):
    array_size_values = []
    time_values = []
    for num in range(5):
        starting_time = datetime.datetime.now()
        for val in range(iterations):
            random_array = [input_words[random.randint(0,len(input_data)-1)] for i in range(array_size)]
            insertion_string(random_array)
        finishing_time = datetime.datetime.now()
        array_size_values.append(array_size)
        time_values.append((finishing_time - starting_time).microseconds)
        print((finishing_time - starting_time).microseconds, " microseconds taken by insertion sort to sort an array of size ", array_size , "for iterations ", iterations)
        array_size *= 10
    return array_size_values, time_values

perforamnce_insertionsort(10,10,input_words)

