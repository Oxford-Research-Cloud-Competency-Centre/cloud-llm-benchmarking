import sys

input = sys.stdin.read
data = input().split()

index = 0
N = int(data[index])
index += 1
M = int(data[index])
index += 1

matrix = []
for _ in range(N):
    row = 0
    for j in range(M + 1):
        val = int(data[index])
        if val:
            row |= (1 << j)
        index += 1
    matrix.append(row)

r = 0
rank = 0
for c in range(M + 1):
    found = -1
    for i in range(r, N):
        if matrix[i] & (1 << c):
            found = i
            break
    if found == -1:
        continue
    matrix[r], matrix[found] = matrix[found], matrix[r]
    for j in range(N):
        if j != r and (matrix[j] & (1 << c)):
            matrix[j] ^= matrix[r]
    rank += 1
    r += 1
    if r == N:
        break

print(rank)