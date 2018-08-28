import random,datetime
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


def perforamnce_quicksort(array_size, iterations, range_start, range_end):
    array_size_values = []
    time_values = []
    for num in range(6):
        sorted_array = [0] * (array_size + 1)
        starting_time = datetime.datetime.now()
        for val in range(iterations):
            random_array = [random.randrange(range_start, range_end, 1) for i in range(array_size)]
            quick_sort(random_array)
        finishing_time = datetime.datetime.now()
        array_size_values.append(array_size)
        time_values.append((finishing_time - starting_time).microseconds)
        print((finishing_time - starting_time).microseconds, " microseconds taken by quicksort to sort an array of size ", array_size , "for iterations ", iterations)
        array_size *= 10
    return array_size_values, time_values

#perforamnce_quicksort(10,10,0,255)
#perforamnce_quicksort(10,10,0,2147483647)
perforamnce_quicksort(10,10,0,9223372036854775807)
