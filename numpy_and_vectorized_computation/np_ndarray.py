import numpy as np

# Generate some random data
data = np.random.randn(2,3)

print(data)

print(data*10)

print(data + data)

# Every array has a shape
print(data.shape)

# and holds homogenous datatype
print(data.dtype)


# Creating ndarrays

data1 = [6,7.5,8,0,1]
arr1 = np.array(data1)
print(arr1)

data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)
print(arr2)
# Looking at the dimention
print(arr2.ndim)
# and shape
print(arr2.shape)

# Create array of zeros
arr_zeros1 = np.zeros(10)
arr_zeros2 = np.zeros((3,6))
print(arr_zeros1,"\n", arr_zeros2)

# Create empty array
arr_empty1 = np.empty((2,3,2))
print(arr_empty1)
# sometimes it returns some uncategorized garbage

# arrange - array-valued version of Python built0in range function
arr_arng = np.arange(15)
print(arr_arng)
