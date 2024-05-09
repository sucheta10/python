# Diagonal Difference:
# Given a square matrix, create a Python program using NumPy that calculates the absolute difference between the sums of its diagonals. For instance, given the matrix:
# Copy code
# 3 2 1
# 4 5 6
# 7 8 9
# The difference would be |(3+5+9) - (1+5+7)| = |17 - 13| = 4.

import numpy as np


def diagonal_absolute_difference(matrix):
    # Calculating the main diagonal sum
    main_diagonal_sum = np.trace(matrix)

    # Calculating the anti-diagonal sum
    anti_diagonal_sum = np.trace(np.flip(matrix, axis=1))

    # Calculating the absolute difference
    absolute_difference = abs(main_diagonal_sum - anti_diagonal_sum)

    return absolute_difference


# Taking user input for the size of the square matrix
n = int(input("Enter the size of the square matrix: "))

# Taking user input for the elements of the square matrix
print("Enter the elements of the square matrix:")
matrix = np.array([list(map(int, input().split())) for _ in range(n)])

# Calculating the absolute difference between the sums of diagonals
result = diagonal_absolute_difference(matrix)

print("Absolute difference between the sums of diagonals:", result)
