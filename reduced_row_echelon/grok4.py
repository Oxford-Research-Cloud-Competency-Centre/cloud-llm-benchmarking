import sys

input = sys.stdin.read
data = input().split()

index = 0
N = int(data[index])
index += 1
M = int(data[index])
index += 1

rows = []
for i in range(N):
    val = 0
    for j in range(M):
        a = int(data[index])
        if a:
            bit = M - j
            val |= (1 << bit)
        index += 1
    b = int(data[index])
    if b:
        val |= 1
    index += 1
    rows.append(val)

# elimination
rank = 0
row_idx = 0
for col in range(M + 1):
    bit = M - col
    pivot = -1
    for i in range(row_idx, N):
        if (rows[i] & (1 << bit)) != 0:
            pivot = i
            break
    if pivot == -1:
        continue
    rows[row_idx], rows[pivot] = rows[pivot], rows[row_idx]
    for i in range(N):
        if i != row_idx and (rows[i] & (1 << bit)) != 0:
            rows[i] ^= rows[row_idx]
    row_idx += 1
    rank += 1

print(rank)