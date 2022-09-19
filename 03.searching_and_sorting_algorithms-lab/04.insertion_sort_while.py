arr = [int(x) for x in input().split()]


def insertions_sort(arr):
    for i in range(len(arr)):
        current = arr[i]

        j = i - 1
        while current < arr[j] and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current

    return arr


print(*insertions_sort(arr))
