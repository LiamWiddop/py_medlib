import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    GREY = '\033[3m'
    FAIL = '\033[1m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class pr:
    color = None
    def __init__(self,*message):
        printEx(self.color,*message)

class Error(pr):
    color = bcolors.FAIL
    sys.stdout.flush()
    def __init__(self,*message):
        super().__init__(*message)

class Alert(pr):
    color = bcolors.BOLD
    def __init__(self,*message):
        super().__init__(*message)

class Header(pr):
    color = bcolors.HEADER
    def __init__(self,*message):
        super().__init__(*message)

class AccessoryError(pr):
    color = bcolors.GREY
    def __init__(self,*message):
        super().__init__(*message)

class Work(pr):
    color = bcolors.OKCYAN
    def __init__(self,*message):
        message = tuple("- ")+message
        super().__init__(*message)


def printEx(code,*message):
    m = ''.join(message)    
    print(code+m+bcolors.ENDC)