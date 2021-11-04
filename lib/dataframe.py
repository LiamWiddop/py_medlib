from lib.manipulator import Manipulator
from lib.html import HTML
from lib.compositor import Compositor
from lib.print import Work,Error,Header

class DataFrameHandler(HTML,Manipulator,Compositor):
    """Super handler for dataframes. Responsible for library imports: MedLib, HTML, Compositor."""
    
    dataframe = None
    unmerged = None

    def __init__(self):
        Header("Initialised DataframeHandler")

    def columns(self) -> list:
        """Returns list of dataframe columns"""
        return self.dataframe.columns.to_list()
    
    def HTMLUnmerged(self):
        if self.unmerged is not None:
            HTML.HTMLRender(self.unmerged)
        else:
            Error("There is no unmerged data")

    def loaded(self):
        Work("Dataframe loaded")