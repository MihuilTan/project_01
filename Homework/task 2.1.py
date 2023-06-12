# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!


arr = [12, 4, 31, -7, 6, 33, 19]
print (arr)

def minimum(arr):
    i=0
    length = len(arr)
    while i < length - 1:
        m = i
        j = i + 1
        while j < length:
            if arr[j]< arr[m]:
                m = j
            j +=1
        arr[i], arr[m] = arr[m], arr[i]
        i += 1
    return arr
print (' -> min', minimum(arr)[0])

def maximum(arr):
    i=0
    length = len(arr)
    while i < length - 1:
        m = i
        j = i + 1
        while j < length:
            if arr[j]< arr[m]:
                m = j
            j +=1
        arr[i], arr[m] = arr[m], arr[i]
        i += 1
    return arr
print (' -> max', maximum(arr)[-1])