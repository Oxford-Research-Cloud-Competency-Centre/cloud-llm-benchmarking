def main():
    import sys
    data = sys.stdin.read().strip().splitlines()
    if not data:
        print(0)
        return
    
    n, m = map(int, data[0].split())
    matrix = []
    for line in data[1:n+1]:
        row = list(map(int, line.split()))
        matrix.append(row)
    
    rows = n
    cols = m + 1
    
    r = 0
    pivots = []
    
    for c in range(cols):
        max_row = -1
        for i in range(r, rows):
            if matrix[i][c] == 1:
                max_row = i
                break
        if max_row == -1:
            continue
            
        matrix[r], matrix[max_row] = matrix[max_row], matrix[r]
        
        pivots.append(c)
        
        for i in range(rows):
            if i != r and matrix[i][c] == 1:
                for j in range(c, cols):
                    matrix[i][j] ^= matrix[r][j]
        
        r += 1
        if r == rows:
            break
            
    rank = sum(1 for row in matrix if any(row))
    print(rank)

if __name__ == "__main__":
    main()