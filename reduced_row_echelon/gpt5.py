import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    cols = M + 1

    rows = []
    for _ in range(N):
        row = 0
        for j in range(cols):
            try:
                val = int(next(it))
            except StopIteration:
                val = 0
            if val & 1:
                row |= 1 << j
        rows.append(row)

    basis = [0] * (cols)
    rank = 0
    for v in rows:
        x = v
        while x:
            msb = x.bit_length() - 1
            b = basis[msb]
            if b:
                x ^= b
            else:
                basis[msb] = x
                rank += 1
                break

    print(rank)

if __name__ == "__main__":
    main()