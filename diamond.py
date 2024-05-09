n = int(input("Enter number of rows: "))
# full pyramid
for i in range(n):
    print(' '*(n-i-1)+'* '*(i+1))
# inverted full pyramid
for j in range(n-1, 0, -1):
    print(' '*(n-j)+'* '*j)