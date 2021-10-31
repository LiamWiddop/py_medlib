import webbrowser
from IPython.display import display
import os

def HTMLRender(target,*args,**kwargs):
    name = kwargs.get('name', None)
    html = None
    filePath = None
    path = None

    # get dataframe target
    if hasattr(target, 'dataframe'):
        target = target.dataframe
    
    # dataframe to html
    html = target.to_html()
    
    # get filename (if supplied) or set unnamed
    if not name and hasattr(target, 'fileName'):
        name = target.fileName

    # set output html file destination and write to
    filePath = './html/'+name+'.html'
    f = open(filePath, "a")
    path = os.path.abspath(filePath)
    with open(path, 'w') as f:
            f.write(html)

    # open in webbrowser
    webbrowser.open(path)