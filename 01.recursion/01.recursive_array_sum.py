#1.	Recursive Array Sum
def calc_sum(arr, idx):
    if idx == len(arr) - 1:
        return arr[idx]
    return arr[idx] + calc_sum(arr, idx + 1)


print(calc_sum([int(x) for x in input().split()], 0))
