
#1.	Recursive Array Sum
def calc_sum(arr, idx):
    if idx == len(arr) - 1:
        return arr[idx]
    return arr[idx] + calc_sum(arr, idx + 1)
#print(calc_sum([int(x) for x in input().split()], 0))
   
#2.	Recursive Factorial
def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)

#print(factorial(int(input())))

#3.	Recursive Drawing
def rec_draw(num):
    if num <= 0:
        return

    print('*' * num)
    rec_draw(num - 1)
    print('#' * num)

#rec_draw(int(input()))

#4.	Generating 0/1 Vectors
# 4-1
# def generate_vectors(arr, idx):
#     if idx >= len(arr):
#         print("".join([str(x) for x in arr]))
#         return
#     for i in range (0, 2):
#         arr[idx] = i
#         generate_vectors(arr, idx + 1)

# generate_vectors([0] * int(input()), 0)

# 4-2
# def gen_01(idx, vector, numbers = 2):
#     if idx >= len(vector):
#         print(*vector, sep='')
#         return
    
#     for num in range(numbers):
#         vector[idx] = num
#         gen_01(idx + 1, vector)
       
# n = int(input())
# vector = [0] * n
# gen_01(0, vector)


#5. Find All Paths in a Labyrinth



