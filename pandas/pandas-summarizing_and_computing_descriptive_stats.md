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
