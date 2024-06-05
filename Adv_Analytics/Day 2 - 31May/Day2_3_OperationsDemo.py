import numpy as np

arr = np.arange(0,10)
print(arr)

# Basic Arithmetic
print(arr + arr)
print(arr * arr)
print(arr - arr)

# This will raise a Warning on division by zero, but not an error !
# It just fill the spot with nan
print(arr/arr)

# Also a warning (but not an error) relating to infinity
print(1/arr)

print(arr**3) 


# Summary statistcs
print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.min())
print(arr.var())
print(arr.std())
