import math


def flip(arr, k):
    pivot = math.floor(k / 2)
    for i in range(0, int(pivot) + 1):
        arr[i], arr[k - i] = arr[k - i], arr[i]


def find_max_val_index(arr, k):
    ans = 0
    for i in range(0, k + 1):
        if arr[i] > arr[ans]:
            ans = i
    return ans


def pancake_sort(arr):
    for i in range(len(arr) - 1, -1, -1):
        max_val_index = find_max_val_index(arr, i)
        flip(arr, max_val_index)
        flip(arr, i)
    return arr
