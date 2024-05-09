n = int(input("Enter number of rows: "))
def hollow_full_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(1, n - i + 1):
            print(" ", end="")

        # Print stars for the first and last rows
        if i == 1 or i == n:
            for j in range(1, 2 * i):
                print("*", end="")
        else:
            # Print stars for hollow part
            for j in range(1, 2 * i):
                if j == 1 or j == 2 * i - 1:
                    print("*", end="")
                else:
                    print(" ", end="")

        print()
hollow_full_pyramid(n)
