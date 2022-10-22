"""A template of useful functions"""

# Don't forget to import modules needed for different functions.
import numpy as np

def create_sorted_string_arr(lst,collumns=3):
    """Convert a list of strings into a sorted array with desired n of colummns."""
    lst = sorted(lst)
    [lst.append("") for i in range(collumns - len(lst)%collumns)]
    rows = int(len(lst)/collumns)
    arr = np.array(lst).reshape(rows,collumns)
    return arr
