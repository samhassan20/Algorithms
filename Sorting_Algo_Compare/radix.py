import datetime, random


def radixsort(mylist):
    maximumrange = False
    digit = 1
    temp = -1
    while not maximumrange:
        maximumrange = True
        buckets = [list() for b in range(10)]   # 10 because for decimal numbers 0-9 buckets

        for i in mylist:
            temp = int(i/digit)
            buckets[temp % 10].append(i)
            if maximumrange and temp > 0:
                maximumrange = False

        c = 0
        for b in range(10):
            for i in buckets[b]:
                mylist[c] = i
                c += 1

        digit *= 10   #next digit


def perforamnce_radixsort(array_size, iterations, range_start, range_end):
    array_size_values = []
    time_values = []
    for num in range(6):
        sorted_array = [0] * (array_size + 1)
        starting_time = datetime.datetime.now()
        for val in range(iterations):
            random_array = [random.randrange(range_start, range_end, 1) for i in range(array_size)]
            radixsort(random_array)
        finishing_time = datetime.datetime.now()
        array_size_values.append(array_size)
        time_values.append((finishing_time - starting_time).microseconds)
        print((finishing_time - starting_time).microseconds, " microseconds taken by Radix sort to sort an array of size ", array_size , "for iterations ", iterations)
        array_size *= 10
    return array_size_values, time_values

#perforamnce_radixsort(10,10,0,255)
#perforamnce_radixsort(10,10,0,2147483647)
perforamnce_radixsort(10,10,0,9223372036854775807)