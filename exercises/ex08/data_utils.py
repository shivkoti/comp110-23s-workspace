from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str,str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a tbale column under a specific header."""
    result: list[str] = []
    #step thorugh table
    for row in table:
        #save every value under key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column header."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of table
    first_row: dict[str, str] = table[0]
    for key in first_row:
    # for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in table:
        values: list[str] = []
        if rows == 0:
            for column in table:
                result[column] = []
            return result
        if rows >= len(table):
            return table
        for elem in range(0, rows):
            values.append(table[column][elem])
        result[column] = values 
    return result
    
           
def select(column_based_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specifc subset of the original columns."""
    result: dict[str, list[str]] = {}
    for elem in column_names:
        result[elem] = column_based_table[elem]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Procuce a new column-based table with two tables combined."""
    result: dict[str, list[str]] = {}
    for column in table_1:
        result[column] = table_1[column]
    for column in table_2:
        if column in result:
            result[column] += table_2[column]
        else:
            result[column] = table_2[column]
    return result


def count(list_1: list[str]) -> dict[str, int]:
    """Counts number of items and list and returns them in dictionary."""
    new_dict = {}
    for elem in list_1:
        if elem not in new_dict:
            new_dict[elem] = 1
        elif elem in new_dict:
            new_dict[elem] += 1
    return new_dict



        









