import webbrowser
from IPython.display import display
import os

def HTMLRender(target,*kwargs):
    name = None
    html = None
    filePath = None
    path = None

    # get dataframe target
    if hasattr(target, 'dataframe'):
        target = target.dataframe
    
    # dataframe to html
    html = target.to_html()
    
    # get filename (if supplied) or set unnamed
    if hasattr(target, 'fileName'):
        name = target.fileName
    else: 
        name = "Unnamed"

    # set output html file destination and write to
    filePath = './html/'+name+'.html'
    f = open(filePath, "a")
    path = os.path.abspath(filePath)
    with open(path, 'w') as f:
            f.write(html)

    # open in webbrowser
    webbrowser.open(path)