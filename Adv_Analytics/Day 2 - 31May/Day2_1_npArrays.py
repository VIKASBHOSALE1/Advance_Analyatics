import numpy as np

my_list = [1,2,3]
my_array = np.array([1,2,3])

print(type(my_list))

#create a numpy array from a list
print(np.array(my_list))
print(type(np.array(my_list)))

#or from a list of lists
my_matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(np.array(my_matrix))

#creating arrays using built-in functions
#Return evenly spaced values within a given interval
#Start,Stop,Step
print(np.arange(0,10))
print(np.arange(0,11,2))

#Generate arrays of zeros or ones
print(np.zeros(3))
print(np.zeros((5,5)))
print(np.ones(3))
print(np.ones((5,5)))

#Return evenly spaced numbers over a specified interval 
#Start,Stop,Number of elements (and not step)
#Unlike numpy.arange(), the stop value is included in the result
#The spacing between values is automatically determined based on the specified number of values (num)
print(np.linspace(0, 10, 3))
print(np.linspace(0, 5, 20))
print(np.linspace(0, 5, 21))

#Random number arrays
print(np.random.rand(2))
print(np.random.rand(5,5))

#From normal distribution
print(np.random.randn(2))
print(np.random.randn(5,5))

# Ramdom integers from low (inclusive) to high (exclusive)
print(np.random.randint(1,100))
print(np.random.randint(-333,222,10))

# Seeding got reproducable results
np.random.seed(77)
print(np.random.rand(4))

np.random.seed(77)
print(np.random.rand(4))

# Storing
arr = np.arange(25)
ranarr = np.random.randint(0,50,10)

print(arr)
print(ranarr)

# reshape : Return an array containing the same data with a new shape
print(arr.reshape(5,5))

# Max, Min and their index positions
print(ranarr.max())
print(ranarr.argmax())
print(ranarr.min())
print(ranarr.argmin())