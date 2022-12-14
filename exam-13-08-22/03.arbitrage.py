from collections import deque

trading_pairs = int(input())

graph = {}
for _ in range(trading_pairs):
    source, target, rate = [x for x in input().split()]
    if source not in graph:
        graph[source] = []
        graph[source].append((target, float(rate)))
    else:
        graph[source].append((target, float(rate)))

target_currency = input()

path = [f'{target_currency}: 1.000']
path_currency = [target_currency]
current_val = 1

queue = deque()
queue.append(target_currency)
visited = set()
while queue:
    current_cur = queue.popleft()
    visited.add(current_cur)

    next_cur, rate = max(graph[current_cur], key=lambda i: i[1])
    current_val = current_val * rate
    path.append(f'{next_cur}: {current_val:.3f}')
    path_currency.append(next_cur)

    # if next_cur in graph:
    if next_cur not in visited:
        queue.append(next_cur)

####
if current_val < 1:
    print("False")
    path.pop()
    print(*path, sep='\n')
elif current_val > 1:
    print("True")
    print(*path_currency, sep=' ')

