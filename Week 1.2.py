##Jesse Zamora
##Week 1 Homework
##DSC 550 T301 Data Mining

import numpy
import numpy as np

# Create 10X50 random array
rand1 = np.random.rand(10,50)

# Calculate sum of rows and place in array
rowsum1 = rand1.sum(axis=1)

# Calculate sum of columns and place in array
colsum1 = rand1.sum(axis=0)

# Original array
print('The original 10X50 random array is: ')
print(rand1)

# Sum of rows
print('Sum of the 10 rows: ')
print(rowsum1)

# Sum of columns
print('Sum of the 50 columns: ')
print(colsum1)

# Minimum value
darr = np.array([rand1])
print('The minimum value of the array is:')
print(darr.min())

# Max value
darr = np.array([rand1])
print('The maximum value of the array is:')
print(darr.max())

# Average value of row
darr = np.array([rand1])
print('The average value of the array rows are:')
avg = sum(rowsum1)/len(rand1)
print(avg)

# Standard Deviation of row
darr = np.array([rand1])
print('The standard deviation of the array rows are:')
stddev = numpy.std(rand1)
print(stddev)

# Average value of column
darr = np.array([rand1])
print('The average value of the array columns are:')
avg = sum(colsum1)/len(rand1)
print(avg)

# Standard Deviation of column
darr = np.array([rand1])
print('The standard deviation of the array columns are:')
stddev = numpy.std(rand1)
print(stddev)

rand2 = np.random.rand(10,50)

rand2_sort = rand2[np.argsort(rand2[:, 1])]

print('The random array sorted by the second column:')
print(rand2_sort)

rand2_sortrow = rand2[np.argsort(rand2[:2, 1])]

print('The random array sorted by the second row:')
print(rand2_sortrow)