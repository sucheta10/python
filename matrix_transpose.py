# Matrix Transposition with Lists and Nested Loops:
# This program transposes a given matrix (converts rows into columns and vice versa).



def matrix_transpose(matrix):

     #Calculating the no. of rows in matrix
    rows = len(matrix)
    #Calculating the no. of columns in matrix
    col = len(matrix[0])
    #New matrix for storing transposed matrix
    transposed_matrix = []

    for j in range(col):
        #Creating new row for each column in the transposed matrix
        transposed_row = []
        for i in range(rows):
              #Appending element at position (i,j) to transposed row
              transposed_row.append(matrix[i][j])
            #Appending transposed row to transposed matrix
        transposed_matrix.append(transposed_row)

    return transposed_matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)


def main():
    rows = int(input("Enter no. of rows:"))
    col = int(input("Enter no. of columns: "))

    matrix = []
    for i in range(rows):
        row = []
        print(f"Enter elements for row {i+1}:")
        for j in range(col):
            element = int(input(f"Enter element {j+1}:"))
            row.append(element)
        matrix.append(row)

    print("Original matrix:")
    print_matrix(matrix)

    transposed_matrix = matrix_transpose(matrix)
    print("Transposed matrix:")
    print_matrix(transposed_matrix)

main()