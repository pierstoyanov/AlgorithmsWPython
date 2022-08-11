from collections import deque

elements = input().split()

size = [0] * len(elements)
previous = [0] * len(elements)
best_size = 0
best_idx = 0


for idx in range(len(elements)):
    current_word = elements[idx]
    current_size = 1
    parent = None

    for prev_idx in range(idx - 1, -1, -1):
        prev_word = elements[prev_idx]

        if len(prev_word) >= len(current_word):
            continue

        if size[prev_idx] + 1 >= current_size:
            current_size = size[prev_idx] + 1
            parent = prev_idx

    size[idx] = current_size
    previous[idx] = parent

    if current_size > best_size:
        best_size = current_size
        best_idx = idx

lis = deque()

idx = best_idx
while idx is not None:
    lis.appendleft(elements[idx])
    idx = previous[idx]

print(*lis, sep=' ')