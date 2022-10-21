# Numerical Python

**Instal Numpy**

`pip3 install numpy`

**Some of the things in NumPy:**

* ndarray - an efficient multidimentional array with arithmetic opperations and flexible broadcasting capabilities
* Mathematical functions for fast ops on arrays of data without loops
* Tools for reading/writing array data to disk, working with memory-maped files
* Linear algebra, random number generation and Fourier transform caabilities.
* A C API for connecting NumPy with libraries written in C, C++, or Fortran.

Numpy by itself does not provide modeling or scientific functionality, but it is a foundamental knowledge for pandas etc.

**Points of focus in study NumPy:**

* Fast vectorized array ops for data minging and cleaning, subseting and filtering, transformation etc
* Array algo's like sorting, unique, and set ops
* Efficient descriptive statistics and aggregating/summarizing data
* Data alignment and relational data manipulations for merging and joining heterogenous datasets
* Expressing conditional logic as array expression instead of loops with *if-elif-else* branches
* Group-wise data manipulation (aggregation, transformatiion, function application)

**Import numpy!!!**

Through this study notes will be many code examples, do not forget to always `import numpy as np` for the examples to work.

## ndarrays

A generic multidimentional container for homogenous data - all the elements must be a same type. 

Allow for fast modification of data:
```python
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
```

Or creating new arrays from other data type:

```python
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
```

ndarray also creates empty arrays or arrays of zeors or ones:

```python
# Create empty array
arr_empty1 = np.empty((2,3,2))
print(arr_empty1)
# sometimes it returns some uncategorized garbage

# Create array of zeros
arr_zeros1 = np.zeros(10)
arr_zeros2 = np.zeros((3,6))
print(arr_zeros1,"\n", arr_zeros2)

# arrange - array-valued version of Python built0in range function
arr_arng = np.arange(15)
print(arr_arng)
```

For more on creation function, see the table int the book *Python for Data Analysis (page 92)*.

### Data Types for ndarrays

***`dtype`*** - special object containing metadata and data about data to help ndarray to interpret the data type in the memory.

Example:
```python
arr1 = np.array([1,2,3], dtype=np.float64)
arr2 = np.array([1,2,3], dtype=np.int64)
```
The data type is most of the time recorded onto underlying disk or memory representation, which makes possible to read and write binary representation and connect to code written in low level languages.
For full listing of Numpy's supported data types, see the table int the book *Python for Data Analysis (page 93)*.

Dtype can be converted or *cast* by `astype` method. Ie cast integers to floats:
```python
arr = np.array([1,2,3,4,5])
float_arr = arr.astype(np.float64)
```
This can be used vise versa as well, but the decimals get truncated. Numerical strings can be astyped into int or float type.

Calling `astype` always make a new array even if the orginal content had the sam dtype.

## Arithmetic with NumPy Arrays

Arrays enable to express batch ops on data wihout writing forloops. Numpy users call it ***vectorization***.
Any arithmetic ops between equal-size arrays apply the op elemt-wise.

```python
arr = np.array([[1.,2.,3.],[4.,5.,6.]])
multiple_x = arr * x
square = arr * arr
substraction_x = arr - x

# scalar arument gets propagated to each element as well
scalar_self = 1 / arr

# arr ** 0.5

```

Comparison between arrays of equal size yield bolean arrays:

```python
#interpreter:
>>> arr1 = np.array([[1.,2.,3.],[4.,5.,6.]])
>>> arr2 = np.array([[0.,4.,1.],[7.,2.,12.]])
>>> arr2 > arr1
array([[False,  True, False],
       [ True, False,  True]])
```
Evaluating ops between different sized arrays is called *broadcasting* (same book, appendix A).

### Basic Indexing and Slicing

**One Dimantional Arrays**

One dimentional arrays are simple as they work the same way like Python lists. 

```python
#interpreter:

>>> arr = np.arange(10)
>>> arr
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> arr[5]
5
>>> arr[5:8]
array([5, 6, 7])
>>> arr[5:8] = 12
>>> arr
array([ 0,  1,  2,  3,  4, 12, 12, 12,  8,  9])
```
If we create a slice from the orgiginal array, its data mutation will reflect in the array itself as well:
```python
>>> arr_slice = arr[5:8]
>>> arr_slice
array([12, 12, 12])
>>> arr 
>>> arr_slice[1] = 12345
>>> arr
array([    0,     1,     2,     3,     4,    12, 12345,    12,     8,    9])
```
Furhter the '*bare*' slice will asign to all values in an array (and all the values the arr_slice represents in the main array.
```python
>>> arr_slice[:] = 64
>>> arr
array([ 0,  1,  2,  3,  4, 64, 64, 64,  8,  9])
```

####Higher Dimentional Arrays

**Two Dimentions**

A basic index returns a one dimentional array of that position, second index points to the value within that array (like in Python lists).
```python
#interpreter:
>>> arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
>>> arr2d[2]
array([7, 8, 9])
>>> arr2d[2][2]
9
```
The common convention is the simplified expression with a comma separation:
```python
>>> arr2d[2, 2]
9
```

**Indexing Elements in NumPy array**

| **INDEX** | **0** | **1** | **2** |
| --- | --- | --- | --- |
| **0** | 0,0 | 0,1 | 0,2 |
| **1** | 1,0 | 1,1 | 1,2 |
| **2** | 2,0 | 2,1 | 2,2 |






