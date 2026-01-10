def gaussian_elimination(matrix):
    n, m = len(matrix), len(matrix[0])
    lead = 0

    for r in range(n):
        if lead >= m:
            break

        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == n:
                i = r
                lead += 1
                if m == lead:
                    return sum(any(row) for row in matrix)

        matrix[i], matrix[r] = matrix[r], matrix[i]

        for i in range(n):
            if i!= r and matrix[i][lead] == 1:
                for j in range(m):
                    matrix[i][j] = (matrix[i][j] + matrix[r][j]) % 2

        lead += 1

    return sum(any(row) for row in matrix)


def main():
    n, _ = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    print(gaussian_elimination(matrix))


if __name__ == "__main__":
    main()