import datetime, random

input_words = []
with open("words.txt") as f:
    lines = f.readlines()
    for val in lines:
        input_words.append(val)

def quick_sort(my_list, start=0, end=None):
    if end is None:
        end = len(my_list) - 1
    def quicksort(my_list, start, end):
        if start >= end:
            return
        pivot = partition(my_list, start, end)
        quicksort(my_list, start, pivot-1)
        quicksort(my_list, pivot+1, end)
    return quicksort(my_list, start, end)

def partition(my_list, start, end):
    pivot = start
    for i in range(start+1, end+1):
        if my_list[i] <= my_list[start]:
            pivot += 1
            my_list[i], my_list[pivot] = my_list[pivot], my_list[i]
    my_list[pivot], my_list[start] = my_list[start], my_list[pivot]
    return pivot


def perforamnce_quick_sort(array_size, iterations, input_data):
    array_size_values = []
    time_values = []
    for num in range(6):
        starting_time = datetime.datetime.now()
        for val in range(iterations):
            random_array = [input_words[random.randint(0,len(input_data)-1)] for i in range(array_size)]
            quick_sort(random_array)
        finishing_time = datetime.datetime.now()
        array_size_values.append(array_size)
        time_values.append((finishing_time - starting_time).microseconds)
        print((finishing_time - starting_time).microseconds, " microseconds taken by quick sort to sort an array of size ", array_size , "for iterations ", iterations)
        array_size *= 10
    return array_size_values, time_values

perforamnce_quick_sort(10,10,input_words)