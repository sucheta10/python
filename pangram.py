
# Pangram Checker with Strings and Conditional Statements:
# This program checks if a given sentence is a pangram (contains every letter of the alphabet at least once).

import string

string = input("Enter a sentence: ")
def pangram(s):
    a = "abcdefghijklmnopqrstuvwxyz"
    for char in a:
        if char not in s.lower():
            return False
    return True

def check():

    if pangram(string):
        print("The sentence is pangram.")
    else:
        print("The sentence is not pangram.")

check()
