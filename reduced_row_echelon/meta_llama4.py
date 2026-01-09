def main():
    try:
        n, m = map(int, input().split())
        matrix = []
        for _ in range(n):
            row = list(map(int, input().split()))
            matrix.append(row)
        rank = compute_rank(matrix)
        print(rank)
    except Exception as e:
        # In a real scenario, you might want to log this error
        pass

def compute_rank(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    row = 0
    col = 0
    rank = 0
    
    while row < num_rows and col < num_cols:
        max_row = row
        for i in range(row, num_rows):
            if matrix[i][col] == 1:
                max_row = i
                break
        else:
            col += 1
            continue
        
        matrix[row], matrix[max_row] = matrix[max_row], matrix[row]
        
        if matrix[row][col] == 0:
            col += 1
            row += 1
            continue
        
        for i in range(num_rows):
            if i != row and matrix[i][col] == 1:
                for j in range(col, num_cols):
                    matrix[i][j] = (matrix[i][j] + matrix[row][j]) % 2
        
        row += 1
        rank += 1
    
    return rank

if __name__ == "__main__":
    main()