# 4.	Generating 0/1 Vectors
def gen_vectors(arr, idx):
    if idx >= len(arr):
        print("".join([str(x) for x in arr]))
        return
    for i in range(0, 2):
        arr[idx] = i
        gen_vectors(arr, idx + 1)


print(gen_vectors([0] * int(input()), 0))
