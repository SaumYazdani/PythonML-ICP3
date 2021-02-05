#importing module
import numpy as np
#setting a matrix to 1 column, 20 rows (20 random element list)
matrix = np.random.rand(1,20)
#setting the elements to 4x5 and saving to new matrix
matrix2 = matrix.reshape((4,5))
#taking the min in each line of the matrix and setting it to 0
matrix2[(np.where(matrix2 == np.min(matrix2[0])))] = 0
matrix2[(np.where(matrix2 == np.min(matrix2[1])))] = 0
matrix2[(np.where(matrix2 == np.min(matrix2[2])))] = 0
matrix2[(np.where(matrix2 == np.min(matrix2[3])))] = 0
#printing the finalized matrix
print (matrix2)
