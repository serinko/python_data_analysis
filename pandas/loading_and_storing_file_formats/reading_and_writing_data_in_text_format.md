# Data Loading

* ***Parsing*** - a term used to describe loading text data and interpreting it as tables and different data types.
* Input and output typically fall into a few main categories: 
    - reading text files and other more efficient on-disk formats
    - loading data from databases
    - interacting with network sources like web APIs

## Reading and Writing Data in Text Format

**Text and binary data loading functions in pandas**

| **Function** | **Description** |
| --- | --- |
| `read_csv` | Load delimited data from a file, URL, or file-like object; use comma as default delimiter |
| `read_fwf` | Read data in fixed-width column format (i.e., no delimiters) |
| `read_clipboard` | Variation of read_csv that reads data from the clipboard; useful for converting tables from web pages |
| `read_excel`	| Read tabular data from an Excel XLS or XLSX file |
| `read_hdf` | Read HDF5 files written by pandas |
| `read_html` | Read all tables found in the given HTML document |
| `read_json` | Read data from a JSON (JavaScript Object Notation) string representation, file, URL, or file-like object |
| `read_feather` | Read the Feather binary file format |
| `read_orc` | Read the Apache ORC binary file format |
| `read_parquet` |  Read the Apache Parquet binary file format |
| `read_pickle`	| Read an object stored by pandas using the Python pickle format |
| `read_sas` | Read a SAS dataset stored in one of the SAS system’s custom storage formats |
| `read_spss` | Read a data file created by SPSS |
| `read_sql` | Read the results of a SQL query (using SQLAlchemy) |
| `read_sql_table` | Eead a whole SQL table (using SQLAlchemy); equivalent to using a query that selects everything in that table using read_sql |
| `read_stata` | Read a dataset from Stata file format |
| `read_xml` | Read a table of data from an XML file |

**Mechanics of the Functions**

* Indexing - treating columns as the returned DataFrame, whether to get column names from the file
* Type inference and data conversion - Includes the user-defined value conversions and custom list of missing value markers
* Date and time parsing - Includes a combining capability, including combining date and time information spread over multiple columns into a single column in the result.
* Iterating - Support for iterating over chunks of very large files.
* Unclean data issues - Includes skipping rows or a footer, comments, or other minor things like numeric data with thousands separated by commas.
  
To deal with the chaotic nature of the data in the world, loading functions (like `pandas.load_csv`) have many optional arguments.
It can be overwhelming and not nessesary to learn them all, always can look into pandas documentation for examples.

```bash
# Checking the example in bash

> cat ex1.csv
a,b,c,d,message
1,2,3,4,hello
5,6,7,8,world
9,10,11,12,foo
```

The example is comma-delimited - we can use `pandas.read_csv` to read it into a DataFrame:

```python
>>> f1 = open("../../../tmp/pydata-book/examples/ex1.csv")
>>> df
   a   b   c   d message
   0  1   2   3   4   hello
   1  5   6   7   8   world
   2  9  10  11  12     foo

```
A file will not always have a header row, like ex2.csv

```bash
> cat ex2.csv
1,2,3,4,hello
5,6,7,8,world
9,10,11,12,foo
```

* Either set pandas to set a default column names or specify them

```python
>>> f2 = open("../../../tmp/pydata-book/examples/ex2.csv")
>>> pd.read_csv(f2, header=None)
   0   1   2   3      4
   0  1   2   3   4  hello
   1  5   6   7   8  world
   2  9  10  11  12    foo
>>> pd.read_csv(f2, names=["a","b","c","d","message"])
      a   b   c   d message
   0  1   2   3   4   hello
   1  5   6   7   8   world
   2  9  10  11  12     foo
```

* in case of asigning the `message` column to be the index of returned DF - either indicate the column at index 4 or named "message" using the `index_col` argument

```python
>>> f2 = open("../../../tmp/pydata-book/examples/ex2.csv")
>>> pd.read_csv(f2, names=names, index_col="message")
a   b   c   d
message
hello    1   2   3   4
world    5   6   7   8
foo      9  10  11  12
```

* For hirarchical index from multiple columns, pass a list of column numbers or names

```bash
> cat csv_mindex.csv
key1,key2,value1,value2
one,a,1,2
one,b,3,4
one,c,5,6
one,d,7,8
two,a,9,10
two,b,11,12
two,c,13,14
two,d,15,16
```
```python
>>> f3 = open("../../../tmp/pydata-book/examples/csv_mindex.csv")
>>> parsed = pd.read_csv(f3, index_col=["key1", "key2"])
>>> parsed
           value1  value2
key1 key2
one  a          1       2
     b          3       4
     c          5       6
     d          7       8
two  a          9      10
     b         11      12
     c         13      14
     d         15      16
```
* Not all cases do have a fixwd delimeter, using whitespace or some other pattern to separate fields:
```bash
> cat ex3.txt
A         B         C
aaa -0.264438 -1.026059 -0.619500
bbb  0.927272  0.302904 -0.032399
ccc -0.264273 -0.386314 -0.217601
ddd -0.871858 -0.348382  1.100491
```
* Possible to fix manualy. The fields in the example are separated by a variable amount of whitespace. A regular expression can be passed, as a delimiter for `pandas.read_csv` - let's use `\s+`:

```python
>>> result = pd.read_csv("ex3.txt",sep="\s+")
>>> result
            A         B         C
aaa -0.264438 -1.026059 -0.619500
bbb  0.927272  0.302904 -0.032399
ccc -0.264273 -0.386314 -0.217601
ddd -0.871858 -0.348382  1.100491
```

In ex3.txt is one fewer column names than the number of data rows, `pandas.read_csv` inferst that the first column should be DF's index in this special case.

* Parsing functions have many additional arguments to handle the exceptions. For example skipping rows with `skiprows` argument:

```bash
> cat ex4.csv
# hey!
a,b,c,d,message
# just wanted to make things more difficult for you
# who reads CSV files with computers, anyway?
1,2,3,4,hello
5,6,7,8,world
9,10,11,12,foo
```

```python
>>> pd.read_csv("ex4.csv", skiprows=[0,2,3])
   a   b   c   d message
0  1   2   3   4   hello
1  5   6   7   8   world
2  9  10  11  12     foo
```
Handling missing values is an important and frequently nuanced part of the file reading process. Missing data is usually either not present (empty string) or marked by some *sentinel* (placeholder) value. By default pandas uses a set of occuring sentinels: `NA` and `NULL`

```bash
> cat ex5.csv
something,a,b,c,d,message
one,1,2,3,4,NA
two,5,6,,8,world
three,9,10,11,12,foo%
```

```python
>>> result = pd.read_csv("ex5.csv")
>>> result
  something  a   b     c   d message
0       one  1   2   3.0   4     NaN
1       two  5   6   NaN   8   world
2     three  9  10  11.0  12     foo
```

* Can be checked with pandas missing values

```python
>>> pd.isna(result)
   something      a      b      c      d  message
0      False  False  False  False  False     True
1      False  False  False   True  False    False
2      False  False  False  False  False    False
```

* The `na_values` option accepts a sequence of strings to add to the default list of strings recognized as missing.

```python
>>> result = pd.read_csv("ex5.csv", na_values=["NULL"])
>>> result
  something  a   b     c   d message
0       one  1   2   3.0   4     NaN
1       two  5   6   NaN   8   world
2     three  9  10  11.0  12     foo
```

* `pandas.read_csv` has many default NA value representations, those can be disabled with the option `keep_default_na`

```python
>>> result2 = pd.read_csv("ex5.csv", keep_default_na=False)
>>> result2
  something  a   b   c   d message
0       one  1   2   3   4      NA
1       two  5   6       8   world
2     three  9  10  11  12     foo
>>> result2.isna()
   something      a      b      c      d  message
0      False  False  False  False  False    False
1      False  False  False  False  False    False
2      False  False  False  False  False    False
>>> result3 = pd.read_csv("ex5.csv", keep_default_na=False, na_values=["NA"])
>>> result3
  something  a   b   c   d message
0       one  1   2   3   4     NaN
1       two  5   6       8   world
2     three  9  10  11  12     foo
>>> result3.isna()
   something      a      b      c      d  message
0      False  False  False  False  False     True
1      False  False  False  False  False    False
2      False  False  False  False  False    False
>>>
```

* Different NA sentinels can be specified for each column in a dictionary

```python
>>> sentinels = {"message": ["foo", "NA"], "something": ["two"]}
>>> pd.read_csv("ex5.csv", na_values=sentinels, keep_default_na=False)
  something  a   b   c   d message
0       one  1   2   3   4     NaN
1       NaN  5   6       8   world
2     three  9  10  11  12     NaN
```

