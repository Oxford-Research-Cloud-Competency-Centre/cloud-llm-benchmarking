import sys

def rank_gf2(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    rank = 0
    for col in range(cols):
        pivot = -1
        for row in range(rank, rows):
            if matrix[row][col] == 1:
                pivot = row
                break
        if pivot == -1:
            continue
        if pivot != rank:
            matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        for row in range(rows):
            if row != rank and matrix[row][col] == 1:
                for c in range(cols):
                    matrix[row][c] ^= matrix[rank][c]
        rank += 1
    return rank

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    matrix = []
    for _ in range(N):
        row = [int(next(it)) for _ in range(M + 1)]
        matrix.append(row)
    print(rank_gf2(matrix))

if __name__ == "__main__":
    main()