import pandas as pd
from lib.print import Error

class PickleHandler:
    def __init__(self,pkl):
        self.load(pkl)

    def load(self,pkl):
        self.location = pkl
        try:
            pklFileArray = self.location.split('/')
            pklFileArrayLen = len(pklFileArray)
            self.fileName = pklFileArray[pklFileArrayLen-1]
            self.pkl = pd.read_pickle(self.location)
            self.dataframe = pd.DataFrame(self.pkl)
        except:
            Error("The provided pkl file destination ("+self.location+") does not exist")

    def print(self):
        print(self.dataframe)

    def columns(self):
        print(self.dataframe.columns)