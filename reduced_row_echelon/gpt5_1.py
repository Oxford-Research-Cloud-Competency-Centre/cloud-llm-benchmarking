import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    mat = []
    for _ in range(N):
        row_int = 0
        for j in range(M + 1):
            bit = int(next(it))
            if bit:
                row_int |= 1 << j
        mat.append(row_int)

    row = 0
    cols = M + 1
    for col in range(cols):
        if row >= N:
            break
        pivot = -1
        mask = 1 << col
        for i in range(row, N):
            if mat[i] & mask:
                pivot = i
                break
        if pivot == -1:
            continue
        mat[row], mat[pivot] = mat[pivot], mat[row]
        for i in range(row + 1, N):
            if mat[i] & mask:
                mat[i] ^= mat[row]
        row += 1

    print(row)

if __name__ == "__main__":
    main()