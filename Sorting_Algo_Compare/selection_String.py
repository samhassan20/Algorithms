import datetime, random

input_words = []
with open("words.txt") as f:
    lines = f.readlines()
    for val in lines:
        input_words.append(val)

def selection_string(data):
    length = len(data)
    for i in range(length-1,0,-1):
        max=0
        for j in range(1,i+1):
            if data[j]>data[max]:
                max = j
        temp = data[i]
        data[i] = data[max]
        data[max] = temp
    return data


def perforamnce_selectionsort(array_size, iterations, input_data):
    array_size_values = []
    time_values = []
    for num in range(6):
        starting_time = datetime.datetime.now()
        for val in range(iterations):
            random_array = [input_words[random.randint(0,len(input_data)-1)] for i in range(array_size)]
            selection_string(random_array)
        finishing_time = datetime.datetime.now()
        array_size_values.append(array_size)
        time_values.append((finishing_time - starting_time).microseconds)
        print((finishing_time - starting_time).microseconds, " microseconds taken by selection sort to sort an array of size ", array_size , "for iterations ", iterations)
        array_size *= 10
    return array_size_values, time_values

perforamnce_selectionsort(10,10,input_words)
