import datetime, random

input_words = []
with open("words.txt") as f:
    lines = f.readlines()
    for val in lines:
        input_words.append(val)

def bubblesort(num_list):
    for i in range(len(num_list)):
        for j in range(len(num_list) - 1, i, -1):
            if (num_list[j] < num_list[j - 1]):
                swap(num_list, j, j - 1)


def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp


def perforamnce_bubble_sort(array_size, iterations, input_data):
    array_size_values = []
    time_values = []
    for num in range(6):
        starting_time = datetime.datetime.now()
        for val in range(iterations):
            random_array = [input_words[random.randint(0,len(input_data)-1)] for i in range(array_size)]
            bubblesort(random_array)
        finishing_time = datetime.datetime.now()
        array_size_values.append(array_size)
        time_values.append((finishing_time - starting_time).microseconds)
        print((finishing_time - starting_time).microseconds, " microseconds taken by bubble sort to sort an array of size ", array_size , "for iterations ", iterations)
        array_size *= 10
    return array_size_values, time_values

perforamnce_bubble_sort(10,10,input_words)
