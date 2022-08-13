from collections import deque

nodes = int(input())
pairs = int(input())

graph = {}
# [graph.append([]) for _ in range(nodes + 1)]

for _ in range(nodes):
    node_str, children_str = input().split(':')
    node = int(node_str)
    children = [int(x) for x in children_str.split()] if children_str else[]
    graph[node] = children

# print(graph)


def find_shortest_path(graph, source, destination):
    queue = deque([source])
    visited = {source}
    parent = {source: None}

    while queue:
        node = queue.popleft()
        if node == destination:
            break
        for child in graph[node]:
            if child in visited:
                continue
            queue.append(child)
            visited.add(child)
            parent[child] = node

    return parent


def find_path_size(parent, destination):
    size = 0
    node = destination
    while node is not None:
        node = parent[node]
        size += 1

    return size - 1


for _ in range(pairs):
    source, destination = [int(x) for x in input().split('-')]

    parent = find_shortest_path(graph, source, destination)

    # queue = deque([source])
    # visited = [False] * len(graph)
    # visited[source] = True
    #
    # parent = [None] * len(graph)

    # while queue:
    #     node = queue.popleft()
    #     if node == destination:
    #         break
    #     for child in graph[node]:
    #         if visited[child]:
    #             continue
    #         queue.append(child)
    #         visited[child] = True
    #         parent[child] = node


    if destination not in parent:
        print(f'{{{source}, {destination}}} -> -1')
        continue

    # #store entire path
    # #path = deque()
    # size = 0
    # node = destination
    # while node is not None:
    #  #   path.appendleft(node)
    #     node = parent[node]
    #     size += 1
    #
    # #print(*path, sep=' ')

    size = find_path_size(parent, destination)
    print(f'{{{source}, {destination}}} -> {size}')
