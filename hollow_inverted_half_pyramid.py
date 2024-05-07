n = int(input("Enter number of rows: "))
def hollow_inverted_half_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(0, i):
            if j == 0 or j == i - 1 or i == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

hollow_inverted_half_pyramid(n)

