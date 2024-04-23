# Simple Calculator:
# Design a simple calculator that takes three inputs from the user: two numbers, and an operator (either +, -, *, or /). Depending on the operator, perform the corresponding operation on the two numbers and print the result. If an invalid operator is entered, print an error message.

def add(n1, n2):
	return n1 + n2
def sub(n1, n2):
	return n1 - n2
def mul(n1, n2):
	return n1 * n2
def div(n1, n2):
	return n1 / n2

print("Select:1)ADD 2)SUBTRACT 3)MULTIPLY 4)DIVIDE")
select = int(input("Select 1, 2, 3, 4 :"))

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if select == 1:
	print(n1, "+", n2, "=",add(n1, n2))
elif select == 2:
	print(n1, "-", n2, "=",sub(n1, n2))
elif select == 3:
	print(n1, "*", n2, "=",mul(n1, n2))
elif select == 4:
	print(n1, "/", n2, "=",div(n1, n2))
else:
	print("Invalid choice")
