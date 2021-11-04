import webbrowser
import os
import time

from lib.print import Alert, Work

class HTML:
    def HTMLRender(self,*args,**kwargs):
        """Parses a dataframe to display as HTML file. Automatically opens in preferred browser when complete."""
        
        Alert("Creating HTML")
        
        html = None
        filePath = None
        path = None
        name = None
        target = None

        # get filename (if supplied) or set from pkl/csv or set as current time
        if 'name' in kwargs:
            name = kwargs.get('name', None)
        elif hasattr(self, 'fileName'):
            name = self.fileName
        else:
            name = str(time.time())

        # get dataframe target
        if hasattr(self, 'dataframe'):
            target = self.dataframe
        else:
            target = self
        
        # dataframe to html
        html = target.to_html()

        # set output html file destination and write to
        filePath = './html/'+name+'.html'
        f = open(filePath, "a")
        path = os.path.abspath(filePath)
        with open(path, 'w') as f:
                f.write(html)

        Work("Complete")

        # open in webbrowser
        Alert("Opening in browser")
        webbrowser.open(path)
        Work("Complete")