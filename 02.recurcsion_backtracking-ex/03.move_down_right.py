rows = int(input())
cols = int(input())

matrix = []
for _ in range(rows):
    matrix.append([0] * cols)
matrix[rows - 1][cols - 1] = 'e'


def find_paths(matrix, r, c):
    if (r >= len(matrix) or c >= len(matrix[0])):
        return 0

    if (matrix[r][c] == 'e'):
        return 1

    result = 0
    # move right
    result += find_paths(matrix, r + 1, c)
    # move down
    result += find_paths(matrix, r, c + 1)
    return result


print(find_paths(matrix, 0, 0))
