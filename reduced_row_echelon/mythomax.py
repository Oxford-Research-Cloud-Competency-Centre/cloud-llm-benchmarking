def rank_matrix_gf2(A, b):
    # Convert matrix A and constant vector b to list of lists
    A_list = [[int(a) for a in row] for row in zip(*A)]
    b_list = [int(b)]
    # Initialize matrix to rows of zeros
    M = len(A_list)
    rank = [0] * (M+1)
    # Iterate over rows of A and b, and solve for x in each row
    for i in range(M):
        # Solve for x in this row
        x = 0
        for j in range(M):
            if A_list[i][j]:
                if A_list[i][j] > x:
                    x = A_list[i][j]
                else:
                    A_list[i][j] = 0
        # If x is not zero, add it to the solution
        if x:
            rank[i+1] = x
    # Return the rank of the augmented matrix
    return len(set(rank[:-1]))