def get_fib_rec(n, memo):
    if (n <= 1):
        return 1

    if n in memo:
        return memo[n]
    else:
        result = get_fib_rec(n - 1, memo) + get_fib_rec(n - 2, memo)
        memo[n] = result 
        return result

n = int(input())

print(get_fib_rec(n, {}))
