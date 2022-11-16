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






