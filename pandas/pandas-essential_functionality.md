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
* `iloc` operatorworks indexes exclusively with integers

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
The row selection syntax data[:2] is provided as a convenience. Passing a single element or a list to the [] operator selects columns.

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


