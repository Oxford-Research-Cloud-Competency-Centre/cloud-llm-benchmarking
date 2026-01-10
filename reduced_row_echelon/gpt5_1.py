import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    cols = M + 1

    rows = []
    for _ in range(N):
        num = 0
        for j in range(cols):
            if next(it) == '1':
                num |= 1 << j
        rows.append(num)

    row = 0
    n = N
    for col in range(cols):
        pivot = row
        while pivot < n and ((rows[pivot] >> col) & 1) == 0:
            pivot += 1
        if pivot == n:
            continue
        rows[row], rows[pivot] = rows[pivot], rows[row]
        for r in range(row + 1, n):
            if (rows[r] >> col) & 1:
                rows[r] ^= rows[row]
        row += 1
        if row == n:
            break

    rank = sum(1 for r in rows if r != 0)
    print(rank)

if __name__ == "__main__":
    main()