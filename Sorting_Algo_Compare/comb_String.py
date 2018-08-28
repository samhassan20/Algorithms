import datetime, random

input_words = []
with open("words.txt") as f:
    lines = f.readlines()
    for val in lines:
        input_words.append(val)

def combSort(data):
    gap = len(data)
    shrink = 1.3
    isSorted = False

    while isSorted is False:
        gap = int(gap / shrink)
        if gap > 1:
            isSorted = False
        else:
            gap = 1
            isSorted = True
        i = 0
        while i + gap < len(data):
            if data[i] > data[i + gap]:
                data[i], data[i + gap] = data[i + gap], data[i]
                isSorted = False
            i += 1
    print(data)
    return data


def perforamnce_comb_sort(array_size, iterations, input_data):
    array_size_values = []
    time_values = []
    for num in range(6):
        starting_time = datetime.datetime.now()
        for val in range(iterations):
            random_array = [input_words[random.randint(0,len(input_data)-1)] for i in range(array_size)]
            combSort(random_array)
        finishing_time = datetime.datetime.now()
        array_size_values.append(array_size)
        time_values.append((finishing_time - starting_time).microseconds)
        print((finishing_time - starting_time).microseconds, " microseconds taken by comb sort to sort an array of size ", array_size , "for iterations ", iterations)
        array_size *= 10
    return array_size_values, time_values

perforamnce_comb_sort(10,10,input_words)