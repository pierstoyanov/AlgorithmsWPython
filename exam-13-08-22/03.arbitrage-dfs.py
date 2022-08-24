from collections import deque, defaultdict

trading_pairs = int(input())

graph = defaultdict(list)
for _ in range(trading_pairs):
    source, target, rate = [x for x in input().split()]
    graph[source].append((target, float(rate)))

target_currency = input()

#path = [f'{target_currency}: 1.000']
#path_currency = [target_currency]

path = []
sum = 1

def DFS(currency, current_sum, visited):

    if currency in visited:


    if currency not in visited:
        path.append((currency, current_sum))
        visited.add(currency)

        for neighbour, rate in graph[currency]:
            DFS(neighbour, current_sum * rate, visited)

x = DFS(target_currency, 1, set())

####
# if current_val < 1:
#     print("False")
#     path.pop()
#     print(*path, sep='\n')
# elif current_val > 1:
#     print("True")
#     print(*path_currency, sep=' ')

