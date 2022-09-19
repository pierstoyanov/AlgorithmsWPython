arr = [int(x) for x in input().split()]


def quick_sort(start, end, arr):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if arr[left] > arr[pivot] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]

        if arr[left] <= arr[pivot]:
            left += 1
        if arr[right] >= arr[pivot]:
            right -= 1

    arr[pivot], arr[right] = arr[right], arr[pivot]
    quick_sort(start, right - 1, arr)
    quick_sort(left, end, arr)


quick_sort(0, len(arr) - 1, arr)
print(*arr, sep=" ")
