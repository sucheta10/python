# Eigenvalues and Eigenvectors Computation:
# Create a program using NumPy to find the eigenvalues and eigenvectors of a given square matrix. The program should display the eigenvalues and the corresponding eigenvectors. Additionally, include a brief explanation in comments on how the eigenvalues and eigenvectors are used in data analysis or other applications.


import numpy as np


def eigen_analysis(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors


def main():
    size = int(input("Enter the size of the square matrix: "))
    print("Enter the elements of the matrix (row-wise):")
    matrix = []
    for _ in range(size):
        row = list(map(float, input().split()))
        matrix.append(row)

    matrix = np.array(matrix)

    eigenvalues, eigenvectors = eigen_analysis(matrix)

    print("\nEigenvalues:")
    for i, eigenvalue in enumerate(eigenvalues):
        print(f"Eigenvalue {i + 1}: {eigenvalue}")

    print("\nEigenvectors:")
    for i, eigenvector in enumerate(eigenvectors.T):  # Transpose eigenvectors matrix for easy iteration
        print(f"Eigenvector {i + 1}:", eigenvector)



main()



# Eigenvalues and eigenvectors are widely used in data analysis. Their applications are:

# 1) Principal Component Analysis (PCA): In data analysis, PCA is a technique used to reduce the dimensionality of data by finding the eigenvectors and eigenvalues of the covariance matrix. These eigenvectors represent the directions of maximum variance in the data, and eigenvalues represent the amount of variance explained by each eigenvector.
# 2) Image Processing: In image processing, eigenvectors and eigenvalues are used for techniques like edge detection, image compression, and feature extraction.
# 3) Mechanical Vibrations: Eigenvalues and eigenvectors are used to analyze the modes of vibration in mechanical systems.
# 4) Quantum Mechanics: In quantum mechanics, eigenvalues and eigenvectors are fundamental to understanding the behavior of quantum systems, representing the possible values of observables and the corresponding states of the system.