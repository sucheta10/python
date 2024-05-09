# Matrix Multiplication Checker:
# Write a Python program using NumPy to check if two matrices can be multiplied. The program should take two matrices as input and return a boolean indicating whether or not they can be multiplied. The program should also perform the multiplication if possible and return the resulting matrix.


import numpy as np

def matrix_multiplication_possible(matrix1, matrix2):
    # Check if the number of columns in matrix1 equals the number of rows in matrix2
    if matrix1.shape[1] == matrix2.shape[0]:
        return True
    else:
        return False

def multiply_matrices(matrix1, matrix2):
    # Performing matrix multiplication
    result = np.matmul(matrix1, matrix2)
    return result

# User input for matrix 1
rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))
print("Enter the elements of the first matrix:")
matrix1 = np.array([list(map(int, input().split())) for _ in range(rows1)])

# User input for matrix 2
rows2 = int(input("Enter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))
print("Enter the elements of the second matrix:")
matrix2 = np.array([list(map(int, input().split())) for _ in range(rows2)])

# Checking if matrices can be multiplied or not and returning boolean form of value
if matrix_multiplication_possible(matrix1, matrix2):
    print("Matrices can be multiplied.")
    # Performing matrix multiplication and returning the resultant matrix
    result_matrix = multiply_matrices(matrix1, matrix2)
    print("Resultant Matrix:")
    print(result_matrix)
else:
    print("Matrices cannot be multiplied.")
