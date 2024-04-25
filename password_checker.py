# Password Strength Checker with String Manipulation and Conditional Statements:
# This program checks the strength of a password based on certain criteria.
# The purpose of the password strength checker program is to assess the strength of a given password based on specific criteria. Here's a breakdown of each criterion:
#
# Length Criterion:
# A strong password should be of sufficient length to resist brute-force attacks. In this program, we consider a password weak if it's less than 8 characters long. A longer password generally provides more security.
# Character Composition Criterion:
# A strong password should contain a mix of different character types, including letters (both uppercase and lowercase), numbers, and special characters. This diversity makes the password more resistant to various hacking techniques, such as dictionary attacks or pattern matching.
# Uppercase and Lowercase Letters Criterion:
# Including both uppercase and lowercase letters enhances password strength by increasing the possible combinations. This criterion ensures that the password is not solely composed of one case, which would make it easier to guess.
# For each criterion, the program checks whether the password satisfies it. If the password fails to meet any of the criteria, it's classified as weak. Otherwise, if it meets all criteria, it's deemed strong.

import string

password = input("Enter your password: ")

def check_password(password):
    #Checking Length Criterion
    if len(password) < 8:
        return False

    # Character Composition Criterion
    lw = any(char.islower() for char in password)
    up = any(char.isupper() for char in password)
    d = any(char.isdigit() for char in password)
    s = any(char in string.punctuation for char in password)

    # Checking Uppercase and Lowercase Letters Criterion
    if not (lw and up):
        return False

    # Checking if all criteria are met
    if d and s:
        return True
    else:
        return False

def check():
    if check_password(password):
        print("Strong password!")
    else:
        print("Weak password!")
        print("Your password must be of atleast 8 characters containg lowercase and uppercase letters alongwith digits and special characters!")

check()
