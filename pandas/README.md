# PANDAS

*As in NumPy, quotes use will be often coming from an interpreter. Tjose cam be recognized by input starting with >>> while output is displayed under, and without the > symbol. *

* Pandas are prefered for data processing without `for loop`s
* Pandas adopts significant parts of array based style computing from NumPy.
* Often used in conjunction with NumPy, SciPy, statsmodels and scikit-learn and matplotlib.

* `pd` will be used for pandas as a common convention. importing some of the major classes into the local namespace dframe is useful.

```python
import pandas as pd
from pandas import Series, DataFrame
```

## Introduction

The most important datastructures are the mentioned ***Series*** and ***DataFrame***. An accessible solution to most of the problems accross the aplications. 

## Series

A Series is one-dimetional array/object with a sequence of values and an associated array of data labels, called *index*.

```python
>>> obj = pd.Series([2,8,-9,4])
>>> obj
0    2
1    8
2   -9
3    4
dtype: int64
```
* Index on the left, values on the right.
* If not specified, index created is from 0 to N - 1 (N is len(values))
* *values* and *index* can be called - *index* will return its attributes

```python
>>> obj.values
array([ 2,  8, -9,  4])
>>> obj.index
RangeIndex(start=0, stop=4, step=1)
```
* Series can be made with index identifying each data point with a label:

```python
>>> obj2 = pd.Series([2,8,-9,4], index=['d','b','a','c'])
>>> obj2
d    2
b    8
a   -9
c    4
dtype: int64
>>> obj2.index
Index(['d', 'b', 'a', 'c'], dtype='object')
```
* Selecting a value or a set of them can be done using labels in the index:

```python
>>> obj2['a']
-9
>>> obj2['d'] = 6
>>> obj2[['c','a','d']]
c    4
a   -9
d    6
dtype: int64

```
* NumPy fns and ops (filtering, boolean array, scalar multiplic, math fns) will preserve the index-value link

```python
>>> obj2[obj2 > 0]
d    6
b    8
c    4
dtype: int64
>>> obj2 * 2
d    12
b    16
a   -18
c     8
dtype: int64
>>> np.exp(obj2)
>>>
>>> import numpy as np
>>>
>>> np.exp(obj2)
d     403.428793
b    2980.957987
a       0.000123
c      54.598150
dtype: float64

```

* Series can be seen as a fixed-length, ordered dict - based on the key-value similar mapping of values to data values.

```python
>>> 'b' in obj2
True
>>> 'e' in obj2
False

```

**Dictionary into Series**

When passing a dict, the index in Series = dict keys

```python
>>> sdata = {'ohio':35000, 'texas':71000, 'oregon':16000, 'utah':5000}
>>> obj3 = pd.Series(sdata)
>>> obj3
ohio      35000
texas     71000
oregon    16000
utah       5000
dtype: int64
```
This can be changed by passing another data and asigning them as index to Series

```python
>>> states = ['california','ohio','oregon','texas']
>>> obj4 = pd.Series(sdata, index=states)
>>> obj4
california        NaN
ohio          35000.0
oregon        16000.0
texas         71000.0
dtype: float64
```
**usnull() & notnull()**

Three values in sdata were asigned, no value for 'california' was found, it appears as NaN (not a number). NaN is Pandas version of *NA* - mark missing.
'utah' was not included in `states`, it is excluded from the resulting object.

Pandas have functions `isnull` and `notnull` to detect missing data.

```python
>>> pd.isnull(obj4)
california     True
ohio          False
oregon        False
texas         False
dtype: bool
>>> 
>>> pd.notnull(obj4)
california    False
ohio           True
oregon         True
texas          True
dtype: bool
>>> 
>>> # Series has those as instance methods too:
>>> 
>>> obj4.isnull()
california     True
ohio          False
oregon        False
texas         False
dtype: bool
```

**automatic index alignment**

One of Series features is the automatic alignment by index label in arithmetic operations, it is similar to join operations in databases.

```python
>>> obj3
ohio      35000
texas     71000
oregon    16000
utah       5000
dtype: int64
>>> 
>>> obj4
california        NaN
ohio          35000.0
oregon        16000.0
texas         71000.0
dtype: float64
>>> 
>>> obj3 + obj4
california         NaN
ohio           70000.0
oregon         32000.0
texas         142000.0
utah               NaN
dtype: float64
```

**name attribute**

Series object and index have a `name` attribute. That integrates other areas of pandas functionality

```python
>>> obj4.name = 'population'
>>> obj4.index.name = 'state'
>>> 
>>> obj4
state
california        NaN
ohio          35000.0
oregon        16000.0
texas         71000.0
Name: population, dtype: float64
```

A Series index can be changed by asignment.

```python
>>> obj
0    2
1    8
2   -9
3    4
dtype: int64
>>> obj.index = ['bob','steve','jeff','ryan']
>>> 
>>> obj
bob      2
steve    8
jeff    -9
ryan     4
dtype: int64
```

## DataFrame

* A DataFrame reresents a rectangular table of data and it contains an ordered collection of columns, each of which can be a different value type (numeric, string, boolean, etc). 
* DataFrame has row and column index. can be seen as a dict of Series all sharing the same index
* The data is stored as one or more two-dimentional blocks rather tham a list, dict etc.
* However physically two dimentional - can represent higher dimentional data in tabular format using hierarchial indexing.

One of the most common ways to construct DataFrame is to approach it from a dict of equal-length ist or NumPy arrays

**Documentation**

There are many methods and attributes which can be used when constructing, modyfying or calling DataFrame. Documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html

```python
>>> data = {'state':['ohio','ohio','ohio', 'nevada','nevada','nevada'], 
...     'year':[2000,2001,2002,2001,2002,2003],
...     'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}
>>>
>>> pd.DataFrame(data)
    state   year  pop
0    ohio  2000  1.5
1    ohio  2001  1.7
2    ohio  2002  3.6
3  nevada  2001  2.4
4  nevada  2002  2.9
5  nevada  2003  3.2
```

`head()` method can be used to select only first five rows.

```python
>>> frame = pd.DataFrame(data)
>>> 
>>> frame.head()
    state   year  pop
0    ohio  2000  1.5
1    ohio  2001  1.7
2    ohio  2002  3.6
3  nevada  2001  2.4
4  nevada  2002  2.9
```

The sequence of columns can be specified to make a different order

```python
>>> pd.DataFrame(data, columns=['year','state','pop'])
    yea   state  pop
0  2000    ohio  1.5
1  2001    ohio  1.7
2  2002    ohio  3.6
3  2001  nevada  2.4
4  2002  nevada  2.9
5  2003  nevada  3.2
```
If a collumn non represented in the dict is passed, it will appear as NaN:

```python
>>> frame2 = pd.DataFrame(data, columns=['year','state','pop','dept'],
...             index=['one','two','three','four','five','six'])
>>> frame2
        yea   state  pop dept
one    2000    ohio  1.5  NaN
two    2001    ohio  1.7  NaN
three  2002    ohio  3.6  NaN
four   2001  nevada  2.4  NaN
five   2002  nevada  2.9  NaN
six    2003  nevada  3.2  NaN

>>> frame2.columns
Index(['year', 'state', 'pop', 'dept'], dtype='object')
```
A column in DataFrame can be retrieved as a Series by dict notation or by attribute:

```python
>>> frame2['state']
one        ohio
two        ohio
three      ohio
four     nevada
five     nevada
six      nevada
Name: state, dtype: object
>>> frame2.year
one      2000
two      2001
three    2002
four     2001
five     2002
six      2003
Name: yea, dtype: int64
```

Rows can be retrieved by position or name with `loc` attribute

```python
>>> frame2.loc['three']
year     2002
state    ohio
pop       3.6
dept      NaN
Name: three, dtype: object
```
Columns can be modified by asignment by a scalar value or an array of values

```python
>>> frame2['dept'] = 16.5
>>> frame2
        year  state  pop  dept
one    2000    ohio  1.5  16.5
two    2001    ohio  1.7  16.5
three  2002    ohio  3.6  16.5
four   2001  nevada  2.4  16.5
five   2002  nevada  2.9  16.5
six    2003  nevada  3.2  16.5
>>> 
>>> frame2['dept'] = np.arange(6.)
>>> frame2
        year  state  pop  dept
one    2000    ohio  1.5   0.0
two    2001    ohio  1.7   1.0
three  2002    ohio  3.6   2.0
four   2001  nevada  2.4   3.0
five   2002  nevada  2.9   4.0
six    2003  nevada  3.2   5.0

```
When asignhning lists or arrays to a column, values length must match the DataFrame length. If you asign Series, its lables will be realigned exactly to the DataFrame index, inserting missing values as NaN.

```python
>>> val = pd.Series([-1.2, -1.5, -1.7], index =['two','four','five'])
>>> frame2['dept'] = val
>>> 
>>> frame2
       year   state  pop  dept
one    2000    ohio  1.5   NaN
two    2001    ohio  1.7  -1.2
three  2002    ohio  3.6   NaN
four   2001  nevada  2.4  -1.5
five   2002  nevada  2.9  -1.7
six    2003  nevada  3.2   Na
```

Asighning a column that does not exist will create a new column. 

```python
>>> frame2['eastern'] = frame2.state == 'ohio'
>>> frame2
       year   state  pop  dept  eastern
one    2000    ohio  1.5   NaN     True
two    2001    ohio  1.7  -1.2     True
three  2002    ohio  3.6   NaN     True
four   2001  nevada  2.4  -1.5    False
five   2002  nevada  2.9  -1.7    False
six    2003  nevada  3.2   NaN    False
```
New columns cannot be created with `frame2.eastern` syntax.

**del method**

`del` will delete columns as with a dict.

```python
>>> del frame2['eastern']
>>> frame2.columns
Index(['year', 'state', 'pop', 'dept'], dtype='object')
```
Columns returned from indexing a DataFrame is a *view* on th underlying data, not a copy. Any modification on the Series will be reflected in the DataFrame. For copy Series's `copy` method is needed.

**Nested dict of dicts**

```python
>>> pop = {'nevada':{2001:2.4,2002:2.9},
...     'ohio':{2000:1.5,2001:1.7,2002:3.6}}

```
If the nested dict is passed to the DataFrame, pandas will interpret the outer dict keys as the columns and the inner as the row indicies

```python
>>> frame3 = pd.DataFrame(pop)
>>> 
>>> frame3
      nevada  ohio
2001     2.4   1.7
2002     2.9   3.6
2000     NaN   1.5
```
***Transpose** using `T` syntax like in numpy

```python
>>> frame3.T
        2001  2002  2000
nevada   2.4   2.9   NaN
ohio     1.7   3.6   1.5
```
The keys in the inner dict are combined and sorted to form the index, unless explicit index is specified.

```python
>>> pd.DataFrame(pop, index=[2001, 2002, 2003])
      nevada  ohio
2001     2.4   1.7
2002     2.9   3.6
2003     NaN   NaN

```
Dicts of Series are treated in a same way

```python
>>> pdata = {'ohio':frame3['ohio'][:-1], 
...     'nevada':frame3['nevada'][:2]}
```
If `index` and `columns` names are set, they will be displayed

```python
>>> frame3.index.name = 'year'; frame3.columns.name  = 'state'
>>> 
>>> frame3
state  nevada  ohio
year               
2001      2.4   1.7
2002      2.9   3.6
2000      NaN   1.5

```
As in Series, the `values` attribute returns the data from DataFrame as a two-dimentional ndarray.

```python
>>> frame3.values
array([[2.4, 1.7],
       [2.9, 3.6],
       [nan, 1.5]])
```

### Index Objects

pandas’s Index objects are responsible for holding the axis labels (including a DataFrame’s column names) and other metadata (like the axis name or names). Any array or other sequence of labels you use when constructing a Series or DataFrame is internally converted to an Index

```python
>>> pd.Series(np.arange(3), index=['a','b','c'])
a    0
b    1
c    2
dtype: int64
>>> obj = pd.Series(np.arange(3), index=['a','b','c'])
>>> index = obj.index
>>> index[1:]
Index(['b', 'c'], dtype='object')
```
Index objects are immutable - cannot be modfied by the user!

```python
>>> index[1] = 'd'
TypeError: Index does not support mutable operations
```
Immutability makes it safer to share Index objects among data structures:

```python
>>> labels = pd.Index(np.arange(3))
>>> labels
Int64Index([0, 1, 2], dtype='int64')
>>> 
>>> obj2 = pd.Series([1.5, -2.5, 0], index=labels)
>>> obj2
0    1.5
1   -2.5
2    0.0
dtype: float64
```


