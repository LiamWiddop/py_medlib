import sys
def Bar(it, prefix="", size=30, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("{}[{}{}] {}%/{}%\r".format('\033[1m'+prefix+'\033[0m \t', "█"*x, " "*(size-x), round((j/count)*100), 100))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield i,item
        show(i+1)
    file.write("\n")
    file.flush()