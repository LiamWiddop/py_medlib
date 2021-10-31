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

class Error:
    def __init__(self,*message):
        print(bcolors.FAIL,"#### ERROR ####",bcolors.ENDC)
        printEx(bcolors.FAIL,*message)

class Alert:
    def __init__(self, message):
        printEx(bcolors.FAIL,message)

class AccessoryError:
    def __init__(self,*message):
        printEx(bcolors.GREY,*message)

def printEx(code,*message):
    for m in message:
        print(code, m, bcolors.ENDC)