def binary_search(arr, target, left_idx, right_idx):
    if right_idx >= left_idx:
        middle_idx = (left_idx + right_idx) // 2

        if target == arr[middle_idx]:
            return middle_idx

        if target < arr[middle_idx]:
            return binary_search(arr, target, left_idx, middle_idx - 1)
        else:
            return binary_search(arr, target, middle_idx + 1, right_idx)

    return -1


nums = [int(x) for x in input().split(' ')]
target = int(input())

print(binary_search(nums, target, 0, len(nums) - 1))
