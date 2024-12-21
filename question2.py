# Exercise 2: Create the specified matrix using for loops
import numpy as np

# Initialize the matrix dimensions
rows, cols = 4, 4
matrix = np.zeros((rows, cols), dtype=int)

for i in range(rows):
    for j in range(cols):
        if (i + j) % 2 == 0:
            matrix[i, j] = -1
        else:
            matrix[i, j] = 1

print("Matrix M:")
print(matrix)
