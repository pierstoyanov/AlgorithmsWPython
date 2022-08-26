class Area:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


def explore_area(matrix, row, col):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[row]):
        return 0

    if matrix[row][col] == '*' or matrix[row][col] == 'v':
        return 0

    result = 1
    matrix[row][col] = 'v'

    result += explore_area(matrix, row + 1, col)  # right
    result += explore_area(matrix, row - 1, col)  # left
    result += explore_area(matrix, row, col + 1)  # down
    result += explore_area(matrix, row, col - 1)  # up

    return result


rows = int(input())
cols = int(input())

matrix = []
for _ in range(rows):
    matrix.append(list(input()))

areas = []
for row in range(rows):
    for col in range(cols):
        size = explore_area(matrix, row, col)
        if size == 0:
            continue
        areas.append(Area(row, col, size))

print(f'Total areas found: {len(areas)}')
for idx, area in enumerate(sorted(areas, key=lambda a: a.size, reverse=True)):
    print(f'Area #{idx + 1} at ({area.row}, {area.col}), size: {area.size}')
