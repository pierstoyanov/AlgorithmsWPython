arr = [int(x) for x in input().split()]


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                swap(arr, i, j)
    return arr



result = selection_sort(arr)

print(*result)
