"""A template of useful functions"""

# Don't forget to import modules needed for different functions.
import numpy as np

def get_sorted_str_array(lst,collumns=3):
    """Convert a list of strings into a sorted array with desired n of colummns."""
    lst = sorted(lst)
    x = columns - len(lst)%columns
    [lst.append("") for i in range(x) if x < columns]
    rows = int(len(lst)/collumns)
    arr = np.array(lst).reshape(rows,collumns)
    return arr
