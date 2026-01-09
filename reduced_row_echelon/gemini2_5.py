import sys

def main():
    try:
        line = sys.stdin.readline()
        if not line.strip():
            print(0)
            return
        N, M = map(int, line.split())
    except (IOError, ValueError):
        print(0)
        return

    if N == 0:
        print(0)
        return
        
    num_cols = M + 1
    
    matrix = []
    for _ in range(N):
        try:
            row_val = 0
            for bit_char in sys.stdin.readline().split():
                row_val = (row_val << 1) | int(bit_char)
            matrix.append(row_val)
        except (IOError, ValueError):
            # In case of malformed input, stop reading
            break
    
    N = len(matrix)
    if N == 0:
        print(0)
        return

    pivot_row = 0
    for j in range(num_cols):
        if pivot_row == N:
            break

        bit_pos = num_cols - 1 - j

        i = pivot_row
        while i < N and not ((matrix[i] >> bit_pos) & 1):
            i += 1

        if i < N:
            matrix[pivot_row], matrix[i] = matrix[i], matrix[pivot_row]
            
            pivot_val = matrix[pivot_row]
            for k in range(N):
                if k != pivot_row and ((matrix[k] >> bit_pos) & 1):
                    matrix[k] ^= pivot_val
            
            pivot_row += 1
            
    print(pivot_row)

if __name__ == "__main__":
    main()