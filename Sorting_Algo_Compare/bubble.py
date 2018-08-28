import random, datetime
def bubblesort(num_list):
    for i in range(len(num_list)):
        for j in range(len(num_list) - 1, i, -1):
            if (num_list[j] < num_list[j - 1]):
                swap(num_list, j, j - 1)


def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp


def perforamnce_bubblesort(array_size, iterations, range_start, range_end):
    array_size_values = []
    time_values = []
    for num in range(5):
        sorted_array = [0] * (array_size + 1)
        starting_time = datetime.datetime.now()
        for val in range(iterations):
            random_array = [random.randrange(range_start, range_end, 1) for i in range(array_size)]
            bubblesort(random_array)
        finishing_time = datetime.datetime.now()
        array_size_values.append(array_size)
        time_values.append((finishing_time - starting_time).microseconds)
        print((finishing_time - starting_time).microseconds, " microseconds taken by quicksort to sort an array of size ", array_size , "for iterations ", iterations)
        array_size *= 10
    return array_size_values, time_values

#perforamnce_bubblesort(10,10,0,255)
#perforamnce_bubblesort(10,10,0,2147483647)
perforamnce_bubblesort(10,10,0,9223372036854775807)
