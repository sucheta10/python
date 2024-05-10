# Rolling Window Average:
# Write a Python function using NumPy to compute the rolling average of a 1D array given the window size. For example, for the array [1, 2, 3, 4, 5] and window size 3, the rolling averages would be [2, 3, 4].

import numpy as np

def rolling_average(array, window_size):
    cumsum = np.cumsum(array, dtype=float)
    cumsum[window_size:] = cumsum[window_size:] - cumsum[:-window_size]
    return cumsum[window_size - 1:] / window_size

def main():
    array = input("Enter the 1D array (space-separated values): ").strip().split()
    array = np.array(list(map(float, array)))
    window_size = int(input("Enter the window size: "))

    if window_size <= 0 or window_size > len(array):
        print("Window size should be a positive integer less than or equal to the length of the array.")
        return

    rolling_avg = rolling_average(array, window_size)
    print("Rolling average:", rolling_avg)


main()
