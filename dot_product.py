#CREATING DOT PRODUCT OF TWO ARRAYS USING NUMPY

import numpy as np

n = int(input("enter size of the two arrays: "))

#Initializing arrays
a1 = np.random.randint(1,10,n)
a2 = np.random.randint(1,10,n)


#Calculating the dot product
dot_product = np.dot(a1, a2)

print("Array 1:", a1)
print("Array 2:", a2)
print("Dot Product using the two arrays: ", dot_product)