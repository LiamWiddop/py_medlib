from typing import List
import pandas as pd
from pandas.core.frame import DataFrame
from lib.print import Alert, Error,AccessoryError,Work
from lib.progress import Bar

class Manipulator:
    def ResetIndex(self):
        self.dataframe.reset_index(drop=True, inplace=True)

    def ColumnMerge(self,columns:list):
        """Receives list of column names to merge series by. Specified columns will display the alike column values per series. 
        \nValues not specified in column list will form fields containing lists of values from all merged series, separated by a comma.
        """
        Alert("Merging columns")
        dataframe = self.dataframe.groupby(columns, as_index=False).agg(lambda x: x.tolist())
        self.dataframe = dataframe
        Work("Complete")
    
    def PopWhere(self,column:str,values:List[str]):
        self.dataframe.drop(self.dataframe.loc[self.dataframe[column].isin(values)].index, inplace=True)
        Work("Complete")
    
    def PopWhereNOT(self,column:str,values:List[str]):
        self.dataframe.drop(self.dataframe.loc[~self.dataframe[column].isin(values)].index, inplace=True)
        Work("Complete")

    def EscapeZeros(self,columnName:str):
        """Escapes zeros from values in specified column. Useful for Medical Record numbers with many leading and trailing zeros."""
        if columnName in self.dataframe:
            try:
                for index,x in Bar(self.dataframe[columnName],"Escaping zeros"):
                    if x.strip().isnumeric():
                        y = x
                        while y[0] == "0":
                            y = y[1:]
                        self.dataframe.replace(to_replace=x, value=y, inplace=True )
            except:
                Error("Issue with escaping zeros")
        else:
            Error("MEDLIB ERROR: Cannot process dataframe: ")
            AccessoryError(self.dataframe)
            Error("Column " + columnName + " Does not exist")

    def RemoveWithout(dataframe:DataFrame,columnName:str,values:list):
        """Removes all series in dataframe where column does not include values."""
        ndf = DataFrame()
        
        if not isinstance(values, list):
            values = [values]
            
        return dataframe