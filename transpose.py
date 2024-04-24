# Matrix Transposition with Lists and Nested Loops:
# This program transposes a given matrix (converts rows into columns and vice versa).
mat = [[1,2],
       [3,4],
       [5,6]]
r = [[0,0,0],
     [0,0,0]]
for i in range(len(mat)):
   for j in range(len(mat[0])):
       r[j][i] = mat[i][j]
for k in r:
   print(k)
