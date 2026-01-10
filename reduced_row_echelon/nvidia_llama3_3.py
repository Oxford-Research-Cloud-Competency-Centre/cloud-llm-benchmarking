def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    matrix = []
    index = 2
    for _ in range(n):
        row = list(map(int, data[index:index + m + 1]))
        index += m + 1
        matrix.append(row)
    
    row = 0
    col = 0
    total_cols = m + 1
    
    while row < n and col < total_cols:
        pivot = -1
        for i in range(row, n):
            if matrix[i][col] == 1:
                pivot = i
                break
        if pivot == -1:
            col += 1
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        for i in range(n):
            if i!= row and matrix[i][col] == 1:
                for j in range(col, total_cols):
                    matrix[i][j] ^= matrix[row][j]
        row += 1
        col += 1
    
    rank = 0
    for r in matrix:
        if any(r):
            rank += 1
    print(rank)

if __name__ == "__main__":
    main()