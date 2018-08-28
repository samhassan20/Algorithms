import datetime, random

input_words = []
with open("words.txt") as f:
    lines = f.readlines()
    for val in lines:
        input_words.append(val)

def cocktailSort(data):
    n = len(data)
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):
        swapped = False
        for i in range(start, end):
            if (data[i] > data[i + 1]):
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
        if (swapped == False):
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if (data[i] > data[i + 1]):
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
        start = start + 1
    return data



def perforamnce_cocktail_sort(array_size, iterations, input_data):
    array_size_values = []
    time_values = []
    for num in range(6):
        starting_time = datetime.datetime.now()
        for val in range(iterations):
            random_array = [input_data[random.randint(0,len(input_data)-1)] for i in range(array_size)]
            cocktailSort(random_array)
        finishing_time = datetime.datetime.now()
        array_size_values.append(array_size)
        time_values.append((finishing_time - starting_time).microseconds)
        print((finishing_time - starting_time).microseconds, " microseconds taken by cocktail sort to sort an array of size ", array_size , "for iterations ", iterations)
        array_size *= 10
    return array_size_values, time_values

perforamnce_cocktail_sort(10,10,input_words)