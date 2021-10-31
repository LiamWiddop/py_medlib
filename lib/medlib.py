import pandas as pd
from lib.print import Error,AccessoryError

def ColumnMergeWithList(dataframe,columns):
    return dataframe.groupby(columns, as_index=False).agg(lambda x: x.tolist())

def EscapeURN(dataframe, columnName):
    if columnName in dataframe:
        for index,x in enumerate(dataframe[columnName]):
            if x.strip().isnumeric():
                while x[0] == "0":
                    x = x[1:]
                dataframe.at[index,columnName]=x
    else:
        Error("MEDLIB ERROR: Cannot process dataframe: ")
        AccessoryError(dataframe)
        Error("Column " + columnName + " Does not exist")