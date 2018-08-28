import datetime, random

input_words = []
with open("words.txt") as f:
    lines = f.readlines()
    for val in lines:
        input_words.append(val)

def mergeSortAlgo(num_list):
    if len(num_list)>1:
        mid = len(num_list)//2
        left_sublist = num_list[:mid]
        right_sublist = num_list[mid:]

        mergeSortAlgo(left_sublist)
        mergeSortAlgo(right_sublist)

        i=0
        j=0
        k=0
        while i < len(left_sublist) and j < len(right_sublist):
            if left_sublist[i] < right_sublist[j]:
                num_list[k]=left_sublist[i]
                i=i+1
            else:
                num_list[k]=right_sublist[j]
                j=j+1
            k=k+1

        while i < len(left_sublist):
            num_list[k]=left_sublist[i]
            i=i+1
            k=k+1

        while j < len(right_sublist):
            num_list[k]=right_sublist[j]
            j=j+1
            k=k+1



def perforamnce_merge_sort(array_size, iterations, input_data):
    array_size_values = []
    time_values = []
    for num in range(6):
        starting_time = datetime.datetime.now()
        for val in range(iterations):
            random_array = [input_words[random.randint(0,len(input_data)-1)] for i in range(array_size)]
            mergeSortAlgo(random_array)
        finishing_time = datetime.datetime.now()
        array_size_values.append(array_size)
        time_values.append((finishing_time - starting_time).microseconds)
        print((finishing_time - starting_time).microseconds, " microseconds taken by merge sort to sort an array of size ", array_size , "for iterations ", iterations)
        array_size *= 10
    return array_size_values, time_values

perforamnce_merge_sort(10,10,input_words)