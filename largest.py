# Write a program that takes three numbers as input and prints the largest one.

a = int (input ("Enter number1: "))
b = int (input ("Enter number2: "))
c = int (input ("Enter number3: "))

if (a>b and a>c):
    print(a,"is largest")
elif (b>c and b>a):
    print(b,"is largest")
else:
    print(c,"is largest")
