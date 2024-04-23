# Grading System:
# Write a Python program that asks the user for their score (0-100) and prints their grade according to the following rules:
# 90-100: A
# 80-89: B
# 70-79: C

n= int(input("Enter marks: "))
if (n >=90 and n <=100):
    print("A")
elif (n>=80 and n<=89):
    print("B")
elif (n>=70 and n<=79):
    print("C")
elif (n>=60 and n<=69):
    print("D")
elif (n>=50 and n<=59):
    print("E")
elif (n>=40 and n<=49):
    print("F")
else:
    print("Fail")