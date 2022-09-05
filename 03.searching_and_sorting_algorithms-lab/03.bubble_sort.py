arr = [int(x) for x in input().split()]


def bubble_sort(arr):
    # Traverse entire arr
    for i in range(len(arr)):
        inner_loop_swapped = False

        for j in range(0, len(arr) - i - 1):
        # traverse until last uncompleted pair
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                inner_loop_swapped = True

        #if no two elements were swapped - i.e. array is ordered
        if inner_loop_swapped == False:
            break


bubble_sort(arr)
print(*arr)
