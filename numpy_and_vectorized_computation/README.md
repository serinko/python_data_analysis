# Numerical Python

**Documentation**

https://numpy.org/doc/

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

#### Higher Dimentional Arrays

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
| **AXES 0:** (vertical) | **AXES 1** | **---->** | **---->** |
| --- | :---: | :---: | :---: |
| **INDEX** | **0** | **1** | **2** |
| **0** | 0,0 | 0,1 | 0,2 |
| **1** | 1,0 | 1,1 | 1,2 |
| **2** | 2,0 | 2,1 | 2,2 |

**Three Dimentions**

A basic index returns two-dimentional array:

```python
#interpreter:

>>> arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
>>> arr3d
array([[[ 1,  2,  3],
        [ 4,  5,  6]],

       [[ 7,  8,  9],
        [10, 11, 12]]])
>>> # arr3d us a 2 x 3 array:
>>> arr3d[0]
array([[1, 2, 3],
       [4, 5, 6]])
>>> # Both scalar values and arrays can be asigned to arr3d[0]:
>>> old_values = arr3d[0].copy()
>>> arr3d
array([[[ 1,  2,  3],
        [ 4,  5,  6]],

       [[ 7,  8,  9],
        [10, 11, 12]]])
>>> arr3d[0]
array([[1, 2, 3],
       [4, 5, 6]])
>>> arr3d[0] = 42
>>> arr3d
array([[[42, 42, 42],
        [42, 42, 42]],

       [[ 7,  8,  9],
        [10, 11, 12]]])
>>> arr3d[0] = old_values
>>> arr3d
array([[[ 1,  2,  3],
        [ 4,  5,  6]],

       [[ 7,  8,  9],
        [10, 11, 12]]])
```

Similarly, two indicies return a one-dimentional array:

```python
>>> arr3d[1,0]
array([7, 8, 9])
>>> # this is a same expression, like indexing in two consecutive steps:
>>> x = arr3d[1]
>>> x
array([[ 7,  8,  9],
       [10, 11, 12]])
>>> x[0]
array([7, 8, 9])
```

**Indexing with Slices**

Like Python lists (one dimention), ndarrays can be sliced with the familiar syntax.

```python
>>> arr
array([ 0,  1,  2,  3,  4, 64, 64, 64,  8,  9])
>>> arr[1:6]
array([ 1,  2,  3,  4, 64])
>>> # slicing 2D array is a bit different:
>>> arr2d
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> arr2d[:2]
array([[1, 2, 3],
       [4, 5, 6]])
```
We can see that it slices along the vertical axis 0, can be read as *"Select the first two rows or arr2d"*.

Multiple sclices, just like multiple indexws may be passed:

```python
>>> arr2d[:2,1:]
array([[2, 3],
       [5, 6]]
```
By mixing integer indexes and slices, return is one dimentional slice. 

```python
>>> arr2d[1,:2]
array([4, 5])
>>> # Optionally select the third column but only the first two rows:
>>> arr2d[:2,2]
array([3, 6])
```
Colon itself means to taje tge entire axis - so only high dimentional axes can be sliced:
```python
>>> arr2d[:,:1]
array([[1],
       [4],
       [7]])
```
Assigning to a slice expression assingns to the whole selection:
```python
>>> arr2d[:2,1:] = 0 
>>> arr2d
array([[1, 0, 0],
       [4, 0, 0],
       [7, 8, 9]])
```

### Boolean Indexing

To explain, we generate an array of duplicating names and a random data one:

```python
>>> import numpy as np
>>> names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
>>> data = np.random.randn(7,4)
>>> names
array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'], dtype='<U4')
>>> data
array([[ 1.01103825,  1.59706866,  0.34615894, -0.13053395],
       [ 0.55175913,  0.32277733, -0.58013767, -0.80211483],
       [ 0.09152834, -0.42857792, -1.95105686,  0.5301571 ],
       [ 0.73288807,  0.32519203, -1.03695664,  0.02228364],
       [-1.05988744, -0.54345945, -0.58454015, -0.63411561],
       [ 0.56522237,  1.29635438,  0.29467277, -0.05104462],
       [ 0.26381219,  0.00957116,  0.03216799, -0.36972802]])
```
Each name corresponds o a row in the data and we want to select all the rowscorresponding with 'Bob'

```python
>>> names == 'Bob'
array([ True, False, False,  True, False, False, False])
```

The boolean array is passed by indexing the array:

```python
>>> data[names == 'Bob']
array([[ 1.01103825,  1.59706866,  0.34615894, -0.13053395],
       [ 0.73288807,  0.32519203, -1.03695664,  0.02228364]])
```
**note:** As the names array is flat - it represents axes 0 for 2D array. Hence the index 'Bob' True (returning True on index 0 and 3 in array names) returns the entire rows (with the same index 0 and 3) from the array data.

This can be combined with selection we used in previous examples (by indexes or slices):

```python
>>> data[names == 'Bob', 2:]
array([[ 0.34615894, -0.13053395],
       [-1.03695664,  0.02228364]])
>>> data[names == 'Bob', 3]
array([-0.13053395,  0.02228364])
```

Select everything but Bob can be done with usual boolean **!=** or negate the condition with **~**:

```python
>>> names != 'Bob'
array([False,  True,  True, False,  True,  True,  True])
>>> data[~(names == 'Bob')]
array([[ 0.55175913,  0.32277733, -0.58013767, -0.80211483],
       [ 0.09152834, -0.42857792, -1.95105686,  0.5301571 ],
       [-1.05988744, -0.54345945, -0.58454015, -0.63411561],
       [ 0.56522237,  1.29635438,  0.29467277, -0.05104462],
       [ 0.26381219,  0.00957116,  0.03216799, -0.36972802]])
```
**~** is good to ivert a general condition:
```python
>>> cond = names == 'Bob'
>>> data[~cond]
array([[ 0.55175913,  0.32277733, -0.58013767, -0.80211483],
       [ 0.09152834, -0.42857792, -1.95105686,  0.5301571 ],
       [-1.05988744, -0.54345945, -0.58454015, -0.63411561],
       [ 0.56522237,  1.29635438,  0.29467277, -0.05104462],
       [ 0.26381219,  0.00957116,  0.03216799, -0.36972802]])
```
To select more names to combine multiple boolean conditions, use boolean arithmetic ops like **& (and)** and **| (or)**:

```python
>>> mask = (names == 'Bob') | (names == 'Will')
>>> mask
array([ True, False,  True,  True,  True, False, False])
>>> data[mask]
array([[ 1.01103825,  1.59706866,  0.34615894, -0.13053395],
       [ 0.09152834, -0.42857792, -1.95105686,  0.5301571 ],
       [ 0.73288807,  0.32519203, -1.03695664,  0.02228364],
       [-1.05988744, -0.54345945, -0.58454015, -0.63411561]])
```
**note:** Selecting by boolean indexing *always* creates a copy of the data - even when returned arr is unchanged. Python key words ('and', 'or') do NOT work with boolean arrays (hence '&' , '|').

Setting values with boolean arrays. Common sense:

```python
# Setting the negative values to 0:
>>> data
array([[1.01103825, 1.59706866, 0.34615894, 0.        ],
       [0.55175913, 0.32277733, 0.        , 0.        ],
       [0.09152834, 0.        , 0.        , 0.5301571 ],
       [0.73288807, 0.32519203, 0.        , 0.02228364],
       [0.        , 0.        , 0.        , 0.        ],
       [0.56522237, 1.29635438, 0.29467277, 0.        ],
       [0.26381219, 0.00957116, 0.03216799, 0.        ]])
```
Similarly we can set whole rows or columns using one-dimentional arr:
```python
>>> data[names != 'Joe'] = 9
>>> data
array([[9.        , 9.        , 9.        , 9.        ],
       [0.55175913, 0.32277733, 0.        , 0.        ],
       [9.        , 9.        , 9.        , 9.        ],
       [9.        , 9.        , 9.        , 9.        ],
       [9.        , 9.        , 9.        , 9.        ],
       [0.56522237, 1.29635438, 0.29467277, 0.        ],
       [0.26381219, 0.00957116, 0.03216799, 0.        ]])
```

These ops on 2d arr's are convenient in Pandas.

### Fancy Indexing

A term adopted by Numpy to use integer arrays for indexing.

```python
>>> arr = np.empty((8,4))
>>> for i in range(8):
...     arr[i] = i
... 
>>> arr
array([[0., 0., 0., 0.],
       [1., 1., 1., 1.],
       [2., 2., 2., 2.],
       [3., 3., 3., 3.],
       [4., 4., 4., 4.],
       [5., 5., 5., 5.],
       [6., 6., 6., 6.],
       [7., 7., 7., 7.]])
```
We ca pass a list or ndarray of int's to select out a subset of the rows in particular order. 
```python
>>> arr[[4,3,6,0]]
array([[4., 4., 4., 4.],
       [3., 3., 3., 3.],
       [6., 6., 6., 6.],
       [0., 0., 0., 0.]])
```
Negative idxs will take rows from the end:

```python
>>> arr[[-3,-5,-7]]
array([[5., 5., 5., 5.],
       [3., 3., 3., 3.],
       [1., 1., 1., 1.]])
```
Passing multiple index arrays retuns one dimentional array of elements corresponding to each tuple of indices.
```python
>>> arr = np.arange(32).reshape((8,4))
>>> arr
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19],
       [20, 21, 22, 23],
       [24, 25, 26, 27],
       [28, 29, 30, 31]])
>>> arr[[1,5,7,2],[0,3,1,2]]
# the elements create tuples of indices
# in our case (1,0), (5,3), (7,1) and (2,2)
# Those applied indexes (axes 0, axes 1), return the value:
array([ 4, 23, 29, 10])
```
Regardless of n of dimentions of arr, the return of fancy indexing is always one-dimentional.

Example from the book, which is needed to be understood:
```python
>>> arr
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19],
       [20, 21, 22, 23],
       [24, 25, 26, 27],
       [28, 29, 30, 31]])
>>> arr[[1,5,7,2]][:,[0,3,1,2]]
array([[ 4,  7,  5,  6],
       [20, 23, 21, 22],
       [28, 31, 29, 30],
       [ 8, 11,  9, 10]]
```
**note:** Fancy indexing always copis data into a new array, not like slicing which changes the value in the originall one. 


### Transposing Arrays and Swapping Axes

Transposingis a form of reshaping - returns a view on the data wythout copying.

`transpose` method and **T** atribute:

```python
>>> arr = np.arange(15).reshape((3,5))
>>> arr
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
>>> 
>>> arr.T
array([[ 0,  5, 10],
       [ 1,  6, 11],
       [ 2,  7, 12],
       [ 3,  8, 13],
       [ 4,  9, 14]])
```

**np.dot()**

[Here](https://www.tutorialspoint.com/numpy/numpy_dot.htm) is the function explained as following:

This function returns the dot product of two arrays. For 2-D vectors, it is the equivalent to matrix multiplication. For 1-D arrays, it is the inner product of the vectors. For N-dimensional arrays, it is a sum product over the last axis of a and the second-last axis of b.

```python
import numpy.matlib 
import numpy as np 

a = np.array([[1,2],[3,4]]) 
b = np.array([[11,12],[13,14]]) 
np.dot(a,b)

# OUTPUT:

[[37  40] 
 [85  92]] 
 
# Authors explanation of the calculation:

[[1*11+2*13, 1*12+2*14],[3*11+4*13, 3*12+4*14]] 
```
Some examples:

```python
>>> arr = np.arange(9).reshape((3,3))
>>> arr2 = arr*2
>>> arr
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
>>> arr2
array([[ 0,  2,  4],
       [ 6,  8, 10],
       [12, 14, 16]])
>>> np.dot(arr,arr2)
array([[ 30,  36,  42],
       [ 84, 108, 132],
       [138, 180, 222]])

>>> arr3 = np.arange(4).reshape((2,2))
>>> arr4 = arr3*2
>>> arr3
array([[0, 1],
       [2, 3]])
>>> arr4
array([[0, 2],
       [4, 6]])
>>> np.dot(arr3,arr4)
array([[ 4,  6],
       [12, 22]])

```

Example from the book combined with **T** `transpose` method:

```python
>>> arr = np.random.randn(6,3)
>>> arr
array([[ 0.30768203, -0.55973789,  0.96629775],
       [-0.80424033, -1.5430307 , -1.29970808],
       [-0.52657437,  0.06968624,  0.95123863],
       [ 0.70538779, -0.48687397,  0.32860383],
       [ 0.2763433 ,  0.8308471 , -1.67640043],
       [ 0.9382419 ,  0.86512439, -0.41448351]])
>>> 
>>> np.dot(arr.T, arr)
array([[ 2.47298674,  1.72991128,  0.22133754],
       [ 1.72991128,  4.37489979, -0.38049662],
       [ 0.22133754, -0.38049662,  6.61792282]])
```

On Higher dimentional arrays - `transpose` will accept a tuple of axis numbers to permute the axes:

```python
>>> arr = np.arange(16).reshape((2,2,4))
>>> arr
array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7]],

       [[ 8,  9, 10, 11],
        [12, 13, 14, 15]]])
>>> 
>>> arr.transpose((1,0,2))
array([[[ 0,  1,  2,  3],
        [ 8,  9, 10, 11]],

       [[ 4,  5,  6,  7],
        [12, 13, 14, 15]]])
```

The result is a re-order with 2nd axis first, 1st axis second and the 3rd axis unchaged. 
ndarray has a method to simply swap axes called `swapaxes` - takes a pair of axis numbers and switches them.

```python
>>> arr
array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7]],

       [[ 8,  9, 10, 11],
        [12, 13, 14, 15]]])
>>> arr.swapaxes(1,2)
array([[[ 0,  4],
        [ 1,  5],
        [ 2,  6],
        [ 3,  7]],

       [[ 8, 12],
        [ 9, 13],
        [10, 14],
        [11, 15]]])
```

No copy was made. 
