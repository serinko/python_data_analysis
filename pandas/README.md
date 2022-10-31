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

### Series

A Series is one-dimetional array/object with a sequence of values and an associated array of data labels, called *index*.

```python
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


