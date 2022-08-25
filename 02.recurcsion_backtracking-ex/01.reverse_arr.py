def reverse_arr(arr, idx):
    # if (len(arr) % 2 == 0):
    #     if idx == int((len(arr) / 2)):
    #         return arr
    # else:
    #     if idx == int((len(arr) / 2) + 1):
    #         return arr

    if idx == len(arr) // 2:
        return arr
    temp = arr[idx]
    arr[idx] = arr[len(arr) - idx - 1]
    arr[len(arr) - idx - 1] = temp

    return reverse_arr(arr, idx + 1)


print(" ".join(reverse_arr([x for x in input().split()], 0)))
