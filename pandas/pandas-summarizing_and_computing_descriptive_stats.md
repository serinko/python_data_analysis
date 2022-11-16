# Summarizing and Computing Descriptive Statistics

## Introduction

* pandas objects are equipped with a set of common mathematical and statistical methods. 
* many are in the category of reductions or summary statistics
    - methods that extract a single value (like the `sum` or `mean`) from a Series
    - a Series of values from the rows or columns of a DataFrame. 
* compared with the similar methods found on NumPy arrays with built-in handling for missing data

```python
>>> import pandas as pd
>>> import numpy as np
>>> 
>>> df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
...     [np.nan, np.nan], [0.75, -1.3]],
...     index=["a", "b", "c", "d"],
...     columns=["one", "two"])
>>> 
>>> df
    one  two
a  1.40  NaN
b  7.10 -4.5
c   NaN  NaN
d  0.75 -1.3

# Calling sum method returns a Series containing column sums 
>>> df.sum()
one    9.25
two   -5.80
dtype: float64

# Passing axis="columns" sums accross columns instead
>>> df.sum(axis="columns")
a    1.40
b    2.60
c    0.00
d   -0.55
dtype: float64
>>> # same result woould be if we pass axis=1
```
If entire row/column coantains NaN values only, the sum = 0. 

* By disabling the option `skipna`, any NaN value in a row or columns names the corresponding result NaN.

```python
>>> df.sum(axis="index", skipna=False)
one   NaN
two   NaN
dtype: float64
>>> 
>>> df.sum(axis="columns", skipna=False)
a     NaN
b    2.60
c     NaN
d   -0.55
dtype: float64
```

**Options for Reduction Methods**

| **Method** | **Description** |
| --- | --- |
| `axis` |	Axis to reduce over; “index” for DataFrame’s rows and “columns” for columns |
| `skipna`	| Exclude missing values; True by default |
| `level` | Reduce grouped by level if the axis is hierarchically indexed (MultiIndex) |

* Methods like `idxmin` and `idxmax` return indirect statistics

```python
>>> df.idxmax()
one    b
two    d
dtype: object
```

* Other methods are *accumulations*

```python
>>> df.cumsum()
    one  two
a  1.40  NaN
b  8.50 -4.5
c   NaN  NaN
d  9.25 -5.8
```

* Some methods are neither reductions nor accumulations. Ie `describe` producing multiple summary statistics in one shot:

```python
>>> df.describe()
            one       two
count  3.000000  2.000000
mean   3.083333 -2.900000
std    3.493685  2.262742
min    0.750000 -4.500000
25%    1.075000 -3.700000
50%    1.400000 -2.900000
75%    4.250000 -2.100000
max    7.100000 -1.300000
```

* On nonnumeric data, `describe` produces alternative summary statistics:

```python
>>> obj = pd.Series(["a", "a", "b", "c"] * 4)
>>> 
>>> obj
0     a
1     a
2     b
3     c
4     a
5     a
6     b
7     c
8     a
9     a
10    b
11    c
12    a
13    a
14    b
15    c
dtype: object
>>> 
>>> obj.describe()
count     16
unique     3
top        a
freq       8
dtype: object
```

**Descriptive and Summary Statistics**

| **Method** |	**Description** |
| --- | --- |
| `count`| Number of non-NA values |
| `describe` | Compute set of summary statistics |
| `min`, `max` | Compute minimum and maximum values |
| `argmin`, `argmax` | Compute index locations (integers) at which minimum or maximum value is obtained, respectively; not available on DataFrame objects
| `idxmin`, `idxmax` | Compute index labels at which minimum or maximum value is obtained, respectively |
| `quantile` | Compute sample quantile ranging from 0 to 1 (default: 0.5) |
| `sum`	| Sum of values |
| `mean`| Mean of values |
| `median` | Arithmetic median (50% quantile) of values |
| `mad`	| Mean absolute deviation from mean value |
| `prod` | Product of all values |
| `var`	| Sample variance of values |
| `std` | Sample standard deviation of values |
| `skew` | Sample skewness (third moment) of values |
| `kurt` | Sample kurtosis (fourth moment) of values |
| `cumsum` | Cumulative sum of values |
| `cummin`, `cummax` | Cumulative minimum or maximum of values, respectively |
| `cumprod`	| Cumulative product of values |
| `diff` | Compute first arithmetic difference (useful for time series) |
| `pct_change` | Compute percent changes |

## Correlation and Covariance

Some summary statistics, like correlation and covariance, are computed from pairs of arguments.

```python
>>> price = pd.read_pickle("../../tmp/pydata-book/examples/yahoo_price.pkl")
>>> volume = pd.read_pickle("../../tmp/pydata-book/examples/yahoo_volume.pkl")
```
* Compute percent changes of the prices, show the *tail*:

```python
>>> returns = price.pct_change()
>>> returns.tail()
                AAPL      GOOG       IBM      MSFT
Date                                              
2016-10-17 -0.000680  0.001837  0.002072 -0.003483
2016-10-18 -0.000681  0.019616 -0.026168  0.007690
2016-10-19 -0.002979  0.007846  0.003583 -0.002255
2016-10-20 -0.000512 -0.005652  0.001719 -0.004867
2016-10-21 -0.003930  0.003011 -0.012474  0.042096
```

* The `corr` method of Series computes the correlation of the overlapping, non-NA, aligned-by-index values in two Series. Relatedly, `cov` computes the covariance:

```python
>>> returns["MSFT"].corr(returns["IBM"])
0.49976361144151144
>>> 
>>> returns["MSFT"].cov(returns["IBM"])
8.870655479703546e-05
```

* DataFrame’s `corr` and `cov` methods, on the other hand, return a full correlation or covariance matrix as a DataFrame, respectively:

```python
>>> returns.corr()
          AAPL      GOOG       IBM      MSFT
AAPL  1.000000  0.407919  0.386817  0.389695
GOOG  0.407919  1.000000  0.405099  0.465919
IBM   0.386817  0.405099  1.000000  0.499764
MSFT  0.389695  0.465919  0.499764  1.000000

>>> returns.cov()
          AAPL      GOOG       IBM      MSFT
AAPL  0.000277  0.000107  0.000078  0.000095
GOOG  0.000107  0.000251  0.000078  0.000108
IBM   0.000078  0.000078  0.000146  0.000089
MSFT  0.000095  0.000108  0.000089  0.000215

```

* DataFrame’s `corrwith` method computes pair-wise correlations between a DataFrame’s columns or rows with another Series or DataFrame. Passing a Series returns a Series with the correlation value computed for each column:

```python
>>> returns.corrwith(returns["IBM"])
AAPL    0.386817
GOOG    0.405099
IBM     1.000000
MSFT    0.499764
```

* Passing a DataFrame computes the correlations of matching column names. Ie correlations of % changes with volume. 

```python
>>> returns.corrwith(volume)
AAPL   -0.075565
GOOG   -0.007067
IBM    -0.204849
MSFT   -0.092950
dtype: float64
```

Passing axis="columns" does it row-by-row. In all cases, the data points are aligned by label before the correlation is computed.

## Unique Values, Value Counts, and Membership

A class of related methods extract information about the values in a one-dimentional Series

* `unique` returns an array of the unique values in a Series:

```python 
>>> obj = pd.Series(["c", "a", "d", "a", "a", "b", "b", "c", "c"])
>>> 
>>> uniques = obj.unique()
>>> uniques
array(['c', 'a', 'd', 'b'], dtype=object)

```
The unique values are not always returned in order they first appeared, neither sorted.

* Can be sorted with `sort()`. `value_counts` computes a SEries containing value frequencies.

```python
>>> uniques.sort()
>>> uniques
array(['a', 'b', 'c', 'd'], dtype=object)
>>> obj.value_counts()
c    3
a    3
b    2
d    1
dtype: int64
```

The Series is sorted by value in descending order as a convenience. 

* `value_counts` is also available as a top level pandas method that can be used with NumPy arrays or other Python squences:

```python
>>> pd.value_counts(obj.to_numpy(), sort=False)
c    3
a    3
d    1
b    2
dtype: int64
```

* `isin` performs a vectorized set membership check and can be useful in filtering a dataset down to a subset of values in a Series or column in a DataFrame:

```python
>>> obj
0    c
1    a
2    d
3    a
4    a
5    b
6    b
7    c
8    c
dtype: object
>>> 
>>> mask = obj.isin(["b", "c"])
>>> 
>>> mask
0     True
1    False
2    False
3    False
4    False
5     True
6     True
7     True
8     True
dtype: bool
>>> 
>>> obj[mask]
0    c
5    b
6    b
7    c
8    c
dtype: object

```

Related to `isin` is the Index.`get_indexer()` method, returns an index array from an array of possibly nondistinct values into another array of distinct values:

```python
>>> to_match = pd.Series(["c", "a", "b", "b", "c", "a"])
>>> unique_vals = pd.Series(["c", "b", "a"])
>>> indices = pd.Index(unique_vals).get_indexer(to_match)
>>> indices
array([0, 2, 1, 1, 0, 2])
```

**Unique, value counts, and set membership methods**

| **Method** | **Description** |
| --- | --- |
| `isin` | Compute a Boolean array indicating whether each Series or DataFrame value is contained in the passed sequence of values |
| `get_indexer` | Compute integer indices for each value in an array into another array of distinct values; helpful for data alignment and join-type operations |
| `unique` | Compute an array of unique values in a Series, returned in the order observed |
| `value_counts` | Return a Series containing unique values as its index and frequencies as its values, ordered count in descending order |

* Example of computing histogram on multiple related columns in a DataFrame:

```python
>>> data = pd.DataFrame({"Qu1": [1, 3, 4, 3, 4],
...     "Qu2": [2, 3, 1, 2, 3],
...     "Qu3": [1, 5, 2, 4, 4]})
>>> data
   Qu1  Qu2  Qu3
0    1    2    1
1    3    3    5
2    4    1    2
3    3    2    4
4    4    3    4

# Compute the value counts for a single column
>>> data["Qu1"].value_counts().sort_index()
1    1
3    2
4    2
Name: Qu1, dtype: int64

# Compute for all columns, pass pandas.value_counts to the DataFrame apply method
>>> result = data.apply(pd.value_counts).fillna(0)
>>> result
   Qu1  Qu2  Qu3
1  1.0  1.0  1.0
2  0.0  2.0  1.0
3  2.0  2.0  0.0
4  2.0  0.0  2.0
5  0.0  0.0  1.0
```

The row labels in the result are the distinct values occurring in all of the columns. The values are the respective counts of these values in each column.

* DataFrame.value_counts method computes counts considering each row of the DataFrame as a tuple to determine the number of occurences of each distinct row.

```python
>>> data = pd.DataFrame({"a": [1, 1, 1, 2, 2], "b": [0, 0, 1, 0, 0]})
>>> data
   a  b
0  1  0
1  1  0
2  1  1
3  2  0
4  2  0
>>> 
>>> data.value_counts()
a  b
1  0    2
2  0    2
1  1    1
dtype: int64
```
The result has an index representing the distinct rows as a hierarchical index.


