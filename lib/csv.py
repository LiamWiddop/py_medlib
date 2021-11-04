import pandas as pd
from lib.print import Error
from lib.dataframe import DataFrameHandler
from lib.print import Work,Alert

class CsvHandler(DataFrameHandler):
    """Receives the location of a .csv file and allows for dataframe manipulation and visualisation from the DataFrameHandler class."""
    def __init__(self,csv:str,*args,**kwargs):
        super().__init__()
        self.load(csv)
        if not 'reset' in kwargs or kwargs.get('reset',True):
            self.ResetIndex()

    def load(self,csv):
        self.location = csv
        try:
            self.csv = pd.read_csv(self.location, header=0)
            csvFileArray = self.location.split('/')
            csvFileArrayLen = len(csvFileArray)
            self.fileName = csvFileArray[csvFileArrayLen-1]
            Alert("Loading dataframe: "+self.fileName)
            self.dataframe = pd.DataFrame(self.csv)
            self.loaded()
        except:
            Error("The provided csv file destination ("+self.location+") does not exist")