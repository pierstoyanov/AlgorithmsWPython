def nested_loops(arr, idx):
    if idx >= len(arr):
        print(*arr, sep=' ')
        return
    for num in range(1, len(arr) + 1):
        arr[idx] = num
        nested_loops(arr, idx + 1)


n = int(input())
arr = [None] * n
nested_loops(arr, 0)
