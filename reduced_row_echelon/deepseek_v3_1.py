def gf2_rank(N, M, matrix):
    rows = N
    cols = M + 1
    rank = 0
    pivot_cols = []
    
    for col in range(cols):
        pivot_row = -1
        for row in range(rank, rows):
            if matrix[row][col] == 1:
                pivot_row = row
                break
        
        if pivot_row == -1:
            continue
        
        matrix[rank], matrix[pivot_row] = matrix[pivot_row], matrix[rank]
        
        for row in range(rows):
            if row != rank and matrix[row][col] == 1:
                for j in range(col, cols):
                    matrix[row][j] ^= matrix[rank][j]
        
        pivot_cols.append(col)
        rank += 1
    
    return rank

def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
    
    N, M = map(int, data[0].split())
    matrix = []
    for i in range(1, 1 + N):
        row = list(map(int, data[i].split()))
        matrix.append(row)
    
    rank = gf2_rank(N, M, matrix)
    print(rank)

if __name__ == "__main__":
    main()