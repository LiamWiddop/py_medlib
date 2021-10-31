import pandas as pd
from lib.print import Error

class CsvHandler:
    def __init__(self,csv):
        self.load(csv)

    def load(self,csv):
        self.location = csv
        try:
            self.csv = pd.read_csv(self.location, header=0)
            csvFileArray = self.location.split('/')
            csvFileArrayLen = len(csvFileArray)
            self.fileName = csvFileArray[csvFileArrayLen-1]
            self.dataframe = pd.DataFrame(self.csv)
        except:
            Error("The provided csv file destination ("+self.location+") does not exist")

    def print(self):
        print(self.dataframe)

    def columns(self):
        print(self.dataframe.columns)