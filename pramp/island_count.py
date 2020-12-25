def get_number_of_islands(binaryMatrix):
    n_rows = len(binaryMatrix)
    n_cols = len(binaryMatrix[0])
    count = 0
    for i in range(n_rows):
        for j in range(n_cols):
            if binaryMatrix[i][j] == 1:
                count += 1
                remove_island(binaryMatrix, i, j)
    return count


def remove_island(binaryMatrix, i, j):
    n_rows = len(binaryMatrix)
    n_cols = len(binaryMatrix[0])

    for (delta_i, delta_j) in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        adj_i = i + delta_i
        adj_j = j + delta_j
        binaryMatrix[i][j] = 0
        if (
            0 <= adj_i < n_rows
            and 0 <= adj_j < n_cols
            and binaryMatrix[adj_i][adj_j] == 1
        ):
            binaryMatrix[adj_i][adj_j] = 0
            remove_island(binaryMatrix, adj_i, adj_j)


""" time complexity: O(n_rows * n_cols) """
""" space complexity: O(n_rows * n_cols) """
