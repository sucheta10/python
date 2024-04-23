# Factorial Calculator:
# Write a program that calculates the factorial of a given number. The factorial of a number n is the product of all positive integers less than or equal to n. For example, the factorial of 5 (5!) is 5 * 4 * 3 * 2 * 1 = 120.

n = int (input ("Enter number to find the factorial: "))
def fact(n):
    if n == 0:
        return 1

    return n * fact(n - 1)

print("Factorial of", n, "is",fact(n))