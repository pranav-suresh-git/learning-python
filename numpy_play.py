
#Numpy_play.py

import numpy as np

# 1. Create an array from a list

x = np.array([1, 2, 3, 4])
print("x:", x)

## Arrays are efficient base data structures for anything math-related
## this 1-D array was created from a Python list [1,2,3,4]


# 2. Create evenly spaced numbers between 0 and 10

#np.linspace(start,stop, number_of_points)
y = np.linspace(0, 10, 5)
print("y (linspace):", y)

# 1-D array
#Creates 5 evenly spaced values from 0-10
    #[0., 2.5, 5., 7.5, 10.]
#Used for creating continuous like inputs (time, space)


# 3. Generate 5 random numbers from a standar normal dist

z = np.random.randn(5)
print("z(random vector):", z)

# 1D array of 5 random numbers from standard normal dist.
#good for simulation, statistics, stochastics

# 4. Element-wise math
print("z-squared:", z ** 2)
# vectorized and no for loop required
# outpute looks like --- z-squared: [array with values squared]

#5. Indexing
print("first element of z:", z[0])
print("last two of x:", x[-2:])

# 6. Aggregate functions
print("mean of z:", np.mean(z))
print("sum of x:", np.sum(x))