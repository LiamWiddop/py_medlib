import pandas as pd
from lib.print import Error
from lib.dataframe import DataFrameHandler
from lib.print import Work,Alert

class PickleHandler(DataFrameHandler):
    """Receives the location of a .pkl file and allows for dataframe manipulation and visualisation from the DataFrameHandler class."""
    def __init__(self,pkl:str,*args,**kwargs):
        super().__init__()
        self.load(pkl)
        if not 'reset' in kwargs or kwargs.get('reset',True):
            self.ResetIndex()

    def load(self,pkl):
        self.location = pkl
        try:
            pklFileArray = self.location.split('/')
            pklFileArrayLen = len(pklFileArray)
            self.fileName = pklFileArray[pklFileArrayLen-1]
            Alert("Loading dataframe: "+self.fileName)
            self.pkl = pd.read_pickle(self.location)
            self.dataframe = pd.DataFrame(self.pkl)
            self.loaded()
        except:
            Error("The provided pkl file destination ("+self.location+") does not exist")