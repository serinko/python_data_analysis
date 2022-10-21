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
