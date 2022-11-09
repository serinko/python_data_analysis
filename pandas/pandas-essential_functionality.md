# Essential Functionality

Fundamental mechanics of interacting with the data contained in a Series or DataFrame like *data anaysis* and *manipulation topics* - using pandas.

## Reindexing

`reindex()` is an important method on pandas object with the values rearranged to align the new index.
Calling the method rearragens the data according to the new index:
```python
>>> obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=["d","b","a","c"])
>>> obj
d    4.5
b    7.2
a   -5.3
c    3.6
dtype: float64
>>> obj2 = obj.reindex(["a","b","c","d","e"])
>>> obj2
a   -5.3
b    7.2
c    3.6
d    4.5
e    NaN
dtype: float64
```
`reindex()` method has an option `ffill` which forward-fills the values

```python
>>> obj3 = pd.Series(["blue", "purple", "yellow"], index=[0, 2, 4])
>>> obj3
0      blue
2    purple
4    yellow
dtype: object
>>> obj3.reindex(np.arange(6), method="ffill")
0      blue
1      blue
2    purple
3    purple
4    yellow
5    yellow
dtype: object
```
With DataFrame, `reindex` can alter the (row) index, columns, or both. When passed only a sequence, it reindexes the rows in the result:

```python
>>> frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
...     index=["a", "c", "d"],
...     columns=["Ohio", "Texas", "California"])
>>> frame
   Ohio  Texas  California
a     0      1           2
c     3      4           5
d     6      7           8
>>> 
>>> frame2 = frame.reindex(index=["a","b","c","d"])
>>> frame2
   Ohio  Texas  California
a   0.0    1.0         2.0
b   NaN    NaN         NaN
c   3.0    4.0         5.0
d   6.0    7.0         8.0
```
`columns` -  a keyword reindexing the columuns.

```python
>>> states = ["Texas", "Utah", "California"]
>>> frame. reindex(columns=states)
   Texas  Utah  California
a      1   NaN           2
c      4   NaN           5
d      7   NaN           8
```

**Reindex Function Arguments**


| **Argument** | **Description** |
| --- | --- |
| `labels`	| New sequence to use as an index. Can be Index instance or any other sequence-like Python data structure. An Index will be used exactly as is without any copying. |
| `index` | Use the passed sequence as the new index labels. |
| `columns` | Use the passed sequence as the new column labels. |
| `axis` | The axis to reindex, whether |
| | `index` (rows) or |
| | `columns`. The default is |
| | `index`. You can alternately do |
| | `reindex(index=new_labels)` or |
| | `reindex(columns=new_labels)`. |
| `method` | Interpolation (fill) method; `ffill` fills forward, while `bfill` fills backward. |
| `fill_value` | Substitute value to use when introducing missing data by reindexing. Use `fill_value="missing"` (the default behavior) when you want absent labels to have null values in the result. |
| `limit` | When forward filling or backfilling, the maximum size gap (in number of elements) to fill. |
| `tolerance` | When forward filling or backfilling, the maximum size gap (in absolute numeric distance) to fill for inexact matches. |
| `level` |	Match simple Index on level of MultiIndex; otherwise select subset of. |
| `copy` | If `True`, always copy underlying data even if the new index is equivalent to the old index; if `False`, do not copy the data when the indexes are equivalent. |

It's possible to reindex by using the `loc` operator, and many users prefer to always do it this way. This works only if all of the new index labels already exist in the DataFrame (whereas reindex will insert missing data for new labels):

```python
>>> frame.loc[["a", "d", "c"], ["California", "Texas"]]
   California  Texas
a           2      1
d           8      7
c           5      4
```

## Dropping Entries from an Axis

Dropping one or more entries from an axis is simple if you already have an index array or list without those entries. `reindex` method or `loc` indexing can be used, `drop` method will return a new object with th indicated value or values deleted from an axis

```python
>>> obj = pd.Series(np.arange(5.), index=["a", "b", "c", "d", "e"])
>>> obj
a    0.0
b    1.0
c    2.0
d    3.0
e    4.0
dtype: float64
>>> new_obj = obj.drop("c")
>>> new_obj
a    0.0
b    1.0
d    3.0
e    4.0
dtype: float64
>>> obj.drop(["d","c"])
a    0.0
b    1.0
e    4.0
dtype: float64
```
With DataFrame, index values can be deleted from either axis

The drop labels can be defined by keywords `index`, `columns`, `axis=<number>` (like in NumPy) or `axis="columns`:

```python
>>> data = pd.DataFrame(np.arange(16).reshape((4, 4)),
...     index=["Ohio", "Colorado", "Utah", "New York"],
...     columns=["one", "two", "three", "four"])
>>> data
          one  two  three  four
Ohio        0    1      2     3
Colorado    4    5      6     7
Utah        8    9     10    11
New York   12   13     14    15
>>> data.drop(index=["Colorado","Ohio"])
          one  two  three  four
Utah        8    9     10    11
New York   12   13     14    15
>>> data.drop(columns=["two"])
          one  three  four
Ohio        0      2     3
Colorado    4      6     7
Utah        8     10    11
New York   12     14    15
>>> 
>>> data.drop("two", axis=1)
          one  three  four
Ohio        0      2     3
Colorado    4      6     7
Utah        8     10    11
New York   12     14    15
>>> 
>>> data.drop(["two","four"], axis="columns")
          one  three
Ohio        0      2
Colorado    4      6
Utah        8     10
New York   12     14
```

## Indexing, Selection, and Filtering

Series indexing (obj[...]) works analogously to NumPy array indexing, except you can use the Series’s index values instead of only integers. Here are some examples of this:

```python
>>> obj = pd.Series(np.arange(4.), index=["a", "b", "c", "d"])
>>> obj
a    0.0
b    1.0
c    2.0
d    3.0
dtype: float64
>>> 
>>> obj['b']
1.0
>>> obj[1]
1.0
>>> obj[2:4]
c    2.0
d    3.0
dtype: float64
>>> obj[["b","a","d"]]
b    1.0
a    0.0
d    3.0
dtype: float64
>>> obj[[1,3]]
b    1.0
d    3.0
dtype: float64
>>> obj[obj < 2]
a    0.0
b    1.0
dtype: float64
```
`loc` is preferable as it treats integers when indexing with `[ ]`. Regular indexing will treat them in that case as labels if the index contains integers, so the behaviour differs depending on the data type of the index.

```python
>>> obj1 = pd.Series([1, 2, 3], index=[2, 0, 1])
>>> obj2 = pd.Series([1, 2, 3], index=["a", "b", "c"])
>>> 
>>> obj1
2    1
0    2
1    3
dtype: int64
>>> 
>>> obj2
a    1
b    2
c    3
dtype: int64
>>> obj1[[0,1,2]]
0    2
1    3
2    1
dtype: int64
>>> obj2[[0,1,2]]
a    1
b    2
c    3
dtype: int64
>>> 
>>># Using loc will fail if the index does not contain integers
>>> 
>>> obj2.loc[[0,1]]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
  raise KeyError(f"None of [{key}] are in the [{axis_name}]")
KeyError: "None of [Int64Index([0, 1], dtype='int64')] are in the [index]"
```

* `loc` operator indexes exclusively with labels
* `iloc` operator indexes exclusively with integers

```python
>>> obj1.iloc[[0,1,2]]
2    1
0    2
1    3
dtype: int64
>>> obj2.iloc[[0,1,2]]
a    1
b    2
c    3
dtype: int64
```

Slicing with labels is possible, but **the endpoint is inclusive!**

```python
>>> obj2.loc["b":"c"]
b    2
c    3
dtype: int64
```

Values can be asigned to a slice - again, ingluding the endpoint

```python
>>> obj2.loc["b":"c"] = 5
>>> obj2
a    1
b    5
c    5
dtype: int64
```

**Indexing into a DataFrame**

Indexing into a DataFrame retrieves one or more columns either with a single value or sequence.

```python
>>> data = pd.DataFrame(np.arange(16).reshape((4, 4)),
...     index=["Ohio", "Colorado", "Utah", "New York"],
...     columns=["one", "two", "three", "four"])
>>> data
          one  two  three  four
Ohio        0    1      2     3
Colorado    4    5      6     7
Utah        8    9     10    11
New York   12   13     14    15

>>> data["two"]
Ohio         1
Colorado     5
Utah         9
New York    13
Name: two, dtype: int64
>>> data[["three","one"]]
          three  one
Ohio          2    0
Colorado      6    4
Utah         10    8
New York     14   12

```

**Special cases of indexing**

1. Slicing or selecting data with Boolean array

```python
>>> data[:2]
          one  two  three  four
Ohio        0    1      2     3
Colorado    4    5      6     7

>>> data[data["three"] > 5]
          one  two  three  four
Colorado    4    5      6     7
Utah        8    9     10    11
New York   12   13     14    15
```
The row selection syntax `data[:2]` is provided as a convenience. Passing a single element or a list to the `[]` operator selects columns.

2. Indexing with a Boolean DataFrame, such as one produced by a scalar comparison

```python
>>> data < 5
            one    two  three   four
Ohio       True   True   True   True
Colorado   True  False  False  False
Utah      False  False  False  False
New York  False  False  False  False
```

Possible to use this DataFrame to assign the value 0 to each location with the value `True`

```python
>>> data[data < 5] = 0
>>> data
          one  two  three  four
Ohio        0    0      0     0
Colorado    0    5      6     7
Utah        8    9     10    11
New York   12   13     14    15
```

**Selection on DataFrame with loc and iloc**

Like Series, DataFrame has special attributes `loc` and `iloc` for label-based and integer-based indexing, respectively. Since DataFrame is two-dimensional, you can select a subset of the rows and columns with NumPy-like notation using either axis labels (loc) or integers (iloc).

* Select a single row by label:

```python
>>> data.loc["Colorado"]
one      0
two      5
three    6
four     7
Name: Colorado, dtype: int64
```

Result of selecting a single row is a Series with index that contains the DataFrame's column lables.

* Pass a sequence of labels to select multiple roles:

```python
>>> data.loc[["Colorado","New York"]]
          one  two  three  four
Colorado    0    5      6     7
New York   12   13     14    15
```

* Combine row and column selection in `loc` by separating the selections with `,`:

```python
>>> data.loc["Colorado",["two","three"]]
two      5
three    6
Name: Colorado, dtype: int64
```

* Perform with integers, using `iloc`, integers select indexes from axis 0:

```python
# single iloc index
>>> data.iloc[2]
one       8
two       9
three    10
four     11
Name: Utah, dtype: int64

# two integers
>>> data.iloc[[2,1]]
          one  two  three  four
Utah        8    9     10    11
Colorado    0    5      6     7

# comma separated lists of indexes [[axis 0],[axis 1]]
>>> data.iloc[2, [3, 0, 1]]
four    11
one      8
two      9
Name: Utah, dtype: int64
>>> data.iloc[[1, 2], [3, 0, 1]]
          four  one  two
Colorado     7    0    5
Utah        11    8    9
```

* `loc` & `iloc` work with slices as well:

```python
>>> data
          one  two  three  four
Ohio        0    0      0     0
Colorado    0    5      6     7
Utah        8    9     10    11
New York   12   13     14    15
>>> 
>>> 
>>> data.loc[:"Utah", "two"]
Ohio        0
Colorado    5
Utah        9
Name: two, dtype: int64
>>> 
>>> data.iloc[:,:3]
          one  two  three
Ohio        0    0      0
Colorado    0    5      6
Utah        8    9     10
New York   12   13     14
>>> 
>>> data.iloc[:,:3][data.three > 5]
          one  two  three
Colorado    0    5      6
Utah        8    9     10
New York   12   13     14
```

* Boolean arrays can be used with `loc` but not `iloc`:

```python
>>> data.loc[data.three >= 2]
          one  two  three  four
Colorado    0    5      6     7
Utah        8    9     10    11
New York   12   13     14    15
```

There are many ways to select and rearrange the data in pandas object.

**Indexing Options with DataFrame**

| **Type** | **Notes** |
| --- | --- |
| `df[column]` | Select single column or sequence of columns from the DataFrame; special case conveniences: Boolean array (filter rows), slice (slice rows), or Boolean DataFrame (set values based on some criterion) |
| `df.loc[rows]` | Select single row or subset of rows from the DataFrame by label |
| `df.loc[:, cols]` | Select single column or subset of columns by label |
| `df.loc[rows, cols]` | Select both row(s) and column(s) by label |
| `df.iloc[rows]` | Select single row or subset of rows from the DataFrame by integer position |
| `df.iloc[:, cols]` | Select single column or subset of columns by integer position |
| `df.iloc[rows, cols]` | Select both row(s) and column(s) by integer position |
| `df.at[row, col]`	| Select a single scalar value by row and column label |
| `df.iat[row, col]` | Select a single scalar value by row and column position (integers) |
| `reindex` method | Select either rows or columns by labels |

**Integer Indexing Pitfalls**

In pandas, objects indexed with integers work differently from built-in Python data structures like lists and tuples. For example, see this error:

```python
>>> ser = pd.Series(np.arange(3.))
>>> ser
0    0.0
1    1.0
2    2.0
dtype: float64
>>> ser[-1]
Traceback (most recent call last):
...
    return self._range.index(new_key)
ValueError: -1 is not in range

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
...
    raise KeyError(key) from err
KeyError: -1
```

DataFrame `ser` has an index containing 0, 1, and 2, but pandas does not want to guess what the user wants (label-based indexing or position-based):

* With a noninteger index, there is no such ambiguity:

```python
>>> ser2 = pd.Series(np.arange(3.), index=["a", "b", "c"])
>>> ser2
a    0.0
b    1.0
c    2.0
dtype: float64
>>> 
>>> ser2[-1]
2.0
```

* Slicing ith integers is always integer oriented:

```python
>>> ser2[:2]
a    0.0
b    1.0
dtype: float64
```

Therefore it's preferable to always indexing with `loc` and `iloc` to avoid this ambiguity.

**Pitfalls with Chained Indexing**

The indexing attributes `loc` & `iloc` can be used to modify DataFrame objects in place, but doing so requires some care.

* Assigning to a column or row by label or integer position, using the example DataFrame above:

```python
>>> data.loc[:,"one"] = 1
>>> data
          one  two  three  four
Ohio        1    0      0     0
Colorado    1    5      6     7
Utah        1    9     10    11
New York    1   13     14    15
>>> 
>>> data.iloc[2] = 5
>>> data
          one  two  three  four
Ohio        1    0      0     0
Colorado    1    5      6     7
Utah        5    5      5     5
New York    1   13     14    15
>>> 
>>> data.loc[data["four"] > 5] = 3
>>> data
          one  two  three  four
Ohio        1    0      0     0
Colorado    3    3      3     3
Utah        5    5      5     5
New York    3    3      3     3

```

* Another possibility with a single `loc` assignment:

```python
>>> data.loc[data.three == 5, "three"] = 6
>>> data
          one  two  three  four
Ohio        1    0      0     0
Colorado    3    3      3     3
Utah        5    5      6     5
New York    3    3      3     3
```
A good rule of thumb is to avoid chained indexing when doing assignments. Aways good to check more in pandas documentation. 

**Arithmetic and Data Alignment**

pandas can make it simpler to work with objects that have different indexes. For example, when you add objects, if any index pairs are not the same, the respective index in the result will be the union of the index pairs.

```python
>>> s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=["a", "c", "d", "e"])
>>> s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1],
...     index=["a", "c", "e", "f", "g"])
>>> 
>>> s1
a    7.3
c   -2.5
d    3.4
e    1.5
dtype: float64
>>> 
>>> s2
a   -2.1
c    3.6
e   -1.5
f    4.0
g    3.1
dtype: float64
>>> 
>>> s1 + s2
a    5.2
c    1.1
d    NaN
e    0.0
f    NaN
g    NaN
dtype: float64
```

The internal data alignment introduces missing values in the label locations that don’t overlap. Missing values will then propagate in further arithmetic computations.

In the case of DataFrame, alignment is performed on both rows and columns:

```python
>>> df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list("bcd"),
...     index=["Ohio","Texas","Colorado"]
... )
>>> 
>>> df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list("bde"),
...     index=["Utah", "Ohio", "Texas", "Oregon"]
... )
>>> 
>>> df1
            b    c    d
Ohio      0.0  1.0  2.0
Texas     3.0  4.0  5.0
Colorado  6.0  7.0  8.0
>>> 
>>> df2
          b     d     e
Utah    0.0   1.0   2.0
Ohio    3.0   4.0   5.0
Texas   6.0   7.0   8.0
Oregon  9.0  10.0  11.0
```
Adding these returns a DataFrame with index and columns that are the unions of the ones in each DataFrame

```python
>>> df1 + df2
            b   c     d   e
Colorado  NaN NaN   NaN NaN
Ohio      3.0 NaN   6.0 NaN
Oregon    NaN NaN   NaN NaN
Texas     9.0 NaN  12.0 NaN
Utah      NaN NaN   NaN NaN
```

Since the *c* and *e* columns are not found in both DataFrame objects, they appear as NaN in the result. The same holds for the rows with labels that are not common to both objects.

* If a DataFrame objects with no column or row labels in common added, the result will contain all nulls:

```python
>>> df1 = pd.DataFrame({"A": [1, 2]})
>>> df2 = pd.DataFrame({"B": [3, 4]})
>>> 
>>> df1
   A
0  1
1  2
>>> 
>>> df2
   B
0  3
1  4
>>> 
>>> df1 + df2
    A   B
0 NaN NaN
1 NaN NaN
```

**Arithmetic Methods with Fill Values**

In arithmetic operations between differently indexed objects is possible to fill with a special value, like 0, when an axis label is found in one object but not the other. 

* Setting a particular value to NA (null) by assigning np.nan to it:

```python
>>> df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list("abcd"))
>>> df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list("abcde"))
>>> 
>>> df2.loc[1,"b"] = np.nan
>>> 
>>> df1
     a    b     c     d
0  0.0  1.0   2.0   3.0
1  4.0  5.0   6.0   7.0
2  8.0  9.0  10.0  11.0
>>> 
>>> df2
      a     b     c     d     e
0   0.0   1.0   2.0   3.0   4.0
1   5.0   NaN   7.0   8.0   9.0
2  10.0  11.0  12.0  13.0  14.0
3  15.0  16.0  17.0  18.0  19.0
>>> 
>>> df1 + df2
      a     b     c     d   e
0   0.0   2.0   4.0   6.0 NaN
1   9.0   NaN  13.0  15.0 NaN
2  18.0  20.0  22.0  24.0 NaN
3   NaN   NaN   NaN   NaN NaN
```

* `add` method on *df1*, passing *df2* and an argument to `fill_value` which substitutes the passed value to any missing values:

```python
>>> df1.add(df2, fill_value=0)
      a     b     c     d     e
0   0.0   2.0   4.0   6.0   4.0
1   9.0   5.0  13.0  15.0   9.0
2  18.0  20.0  22.0  24.0  14.0
3  15.0  16.0  17.0  18.0  19.0
```

* each method has a counterpart starting with `r`,  that has arguments reversed. ie following statements are equivalent:

```python
>>> 1 / df1
       a         b         c         d
0    inf  1.000000  0.500000  0.333333
1  0.250  0.200000  0.166667  0.142857
2  0.125  0.111111  0.100000  0.090909
>>> df1.rdiv(1)
       a         b         c         d
0    inf  1.000000  0.500000  0.333333
1  0.250  0.200000  0.166667  0.142857
2  0.125  0.111111  0.100000  0.090909
```

* Possible to specify a different fill value, when reindexing a Series or DataFrame:

```python
>>> df1.reindex(columns=df2.columns, fill_value=0)
     a    b     c     d  e
0  0.0  1.0   2.0   3.0  0
1  4.0  5.0   6.0   7.0  0
2  8.0  9.0  10.0  11.0  0
```

**Flexible Arithmetic Methods**

| **Method** | **Description** |
| --- | --- |
| `add`, `radd`	| Methods for addition (+) |
| `sub`, `rsub`	| Methods for subtraction (-) |
| `div`, `rdiv`	| Methods for division (/) |
| `floordiv`, `rfloordiv` |	Methods for floor division (//) |
| `mul`, `rmul`	| Methods for multiplication (*) |
| `pow`, `rpow`	| Methods for exponentiation (**) |

**Operations between DataFrame and Series**

As with NumPy arrays of different dimensions, arithmetic between DataFrame and Series is also defined. 

* A difference between a two-dimensional array and one of its rows:

```python
>>> arr = np.arange(12.).reshape((3, 4))
>>> 
>>> arr
array([[ 0.,  1.,  2.,  3.],
       [ 4.,  5.,  6.,  7.],
       [ 8.,  9., 10., 11.]])
>>> 
>>> arr[0]
array([0., 1., 2., 3.])
>>> 
>>> arr - arr[0]
array([[0., 0., 0., 0.],
       [4., 4., 4., 4.],
       [8., 8., 8., 8.]])
```

Subtracting `arr[0]` from `arr` - the subtraction is performed once for each row. This is referred to as *broadcasting* and relates to general NumPy arrays.

* Operations between a DataFrame and a Series are similar

```python
>>> frame = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list("bde"),
...     index=["Utah", "Ohio", "Texas", "Oregon"])
>>> 
>>> series = frame.iloc[0]
>>> 
>>> frame
          b     d     e
Utah    0.0   1.0   2.0
Ohio    3.0   4.0   5.0
Texas   6.0   7.0   8.0
Oregon  9.0  10.0  11.0
>>> 
>>> series
b    0.0
d    1.0
e    2.0
Name: Utah, dtype: float64
```

* By default, arithmetic between DataFrame and Series matches the index of the Series on the columns of the DataFrame, broadcasting down the rows:

```python
>>> frame - series
          b    d    e
Utah    0.0  0.0  0.0
Ohio    3.0  3.0  3.0
Texas   6.0  6.0  6.0
Oregon  9.0  9.0  9.0
```

* If an index value is not found in either the DataFrame’s columns or the Series’s index, the objects will be reindexed to form the union:

```python
>>> series2 = pd.Series(np.arange(3), index=["b", "e", "f"])
>>> series2
b    0
e    1
f    2
dtype: int64
>>> 
>>> frame+series2
          b   d     e   f
Utah    0.0 NaN   3.0 NaN
Ohio    3.0 NaN   6.0 NaN
Texas   6.0 NaN   9.0 NaN
Oregon  9.0 NaN  12.0 NaN
```

* It's possible to broadcast over the columns, matching on the rows - use one of the arithmetic methods and specify to match over the index:

```python
>>> series3 = frame["d"]
>>> frame
          b     d     e
Utah    0.0   1.0   2.0
Ohio    3.0   4.0   5.0
Texas   6.0   7.0   8.0
Oregon  9.0  10.0  11.0
>>> series3
Utah       1.0
Ohio       4.0
Texas      7.0
Oregon    10.0
Name: d, dtype: float64
>>> frame.sub(series3, axis='index')
          b    d    e
Utah   -1.0  0.0  1.0
Ohio   -1.0  0.0  1.0
Texas  -1.0  0.0  1.0
Oregon -1.0  0.0  1.0
```

The axis passed is the axis to match on. In this case the match is on the DataFrame’s row index (axis="index") and broadcast across the columns.


**Function Application and Mapping**

NumPy ufuncs (element-wise array methods) also work with pandas objects

```python
>>> frame = pd.DataFrame(np.random.standard_normal((4, 3)),
...     columns=list("bde"), index=["Utah", "Ohio", "Texas", "Oregon"])
>>> frame
               b         d         e
Utah   -0.194371 -2.524847  0.487050
Ohio    0.392791  0.630667  2.300653
Texas  -0.776571  0.282784  0.127677
Oregon  0.964615  0.974784  1.205621
>>> 
>>> np.abs(frame)
               b         d         e
Utah    0.194371  2.524847  0.487050
Ohio    0.392791  0.630667  2.300653
Texas   0.776571  0.282784  0.127677
Oregon  0.964615  0.974784  1.205621
```

* A frequent operation is applying a function on one-dimensional arrays to each column or row. DataFrame’s apply method does exactly this:

```python
>>> def f1(x):
...     return x.max() - x.min()
... 
>>> frame.apply(f1)
b    1.741186
d    3.499632
e    2.172976
dtype: float64
```

The function `f`, which computes the difference between the maximum and minimum of a Series, is invoked once on each column in `frame`. The result is a Series having the columns of frame as its index.

If passed `axis="columns"` to apply, the function will be invoked once per row instead. A helpful way to think about this is as “apply across the columns”.

```python
>>> frame.apply(f1, axis="columns")
Utah      3.011897
Ohio      1.907862
Texas     1.059355
Oregon    0.241006
dtype: float64
```
Many of the most common array statistics (like `sum` and `mean`) are DataFrame methods, so using `apply` is not necessary.

* The function passed to `apply` need not return a scalar value; it can also return a Series with multiple values:

```python
>>> def f2(x):
...     return pd.Series([x.min(), x.max()], index=["min", "max"])
... 
>>> frame.apply(f2)
            b         d         e
min -0.776571 -2.524847  0.127677
max  0.964615  0.974784  2.300653

```
Element-wise Python functions can be used, too. Ie to compute a formatted string from each floating-point value in frame. Use `applymap`:

```python
>>> def my_format(x):
...     return f"{x:.2f}"
... 
>>> frame.applymap(my_format)
            b      d     e
Utah    -0.19  -2.52  0.49
Ohio     0.39   0.63  2.30
Texas   -0.78   0.28  0.13
Oregon   0.96   0.97  1.21
```

* The name applymap is because Series has a map method for applying an element-wise function:

```python
>>> frame["e"].map(my_format)
Utah      0.49
Ohio      2.30
Texas     0.13
Oregon    1.21
Name: e, dtype: object
```




