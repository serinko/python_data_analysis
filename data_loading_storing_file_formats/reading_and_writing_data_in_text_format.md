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


