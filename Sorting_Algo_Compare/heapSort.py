import random, datetime
def heapsort(data):
    # convert aList to heap
    length = len(data) - 1
    leastParent = length / 2
    for i in range(int(leastParent), -1, -1):
        heapify(data, i, length)

    # flatten heap into sorted array
    for i in range(length, 0, -1):
        if data[0] > data[i]:
            swap(data, 0, i)
            heapify(data, 0, i - 1)


def heapify(data, first, last):
    largest = 2 * first + 1
    while largest <= last:
        # right child exists and is larger than left child
        if (largest < last) and (data[largest] < data[largest + 1]):
            largest += 1

        # right child is larger than parent
        if data[largest] > data[first]:
            swap(data, largest, first)
            # move down to largest child
            first = largest;
            largest = 2 * first + 1
        else:
            return  # force exit

def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp



def perforamnce_heapsort(array_size, iterations, range_start, range_end):
    array_size_values = []
    time_values = []
    for num in range(6):
        sorted_array = [0] * (array_size + 1)
        starting_time = datetime.datetime.now()
        for val in range(iterations):
            random_array = [random.randrange(range_start, range_end, 1) for i in range(array_size)]
            heapsort(random_array)
        finishing_time = datetime.datetime.now()
        array_size_values.append(array_size)
        time_values.append((finishing_time - starting_time).microseconds)
        print((finishing_time - starting_time).microseconds, " microseconds taken by selection sort to sort an array of size ", array_size , "for iterations ", iterations)
        array_size *= 10
    return array_size_values, time_values

#perforamnce_heapsort(10,10,0,255)
#perforamnce_heapsort(10,10,0,2147483647)
perforamnce_heapsort(10,10,0,9223372036854775807)
