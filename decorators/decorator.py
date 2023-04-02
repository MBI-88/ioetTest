import re,os,sys


pathRe = re.compile(r'\.txt$')

def cleanData(f) -> object:
    """
        This decorator is for checking the path.
    """
    def wrapper(args:str) -> object:
        if pathRe.search(args) and os.path.isfile(args):
            return f(args)
        else:
            print("Error file")
            exit(1)
    return wrapper


@cleanData
def readData(path:str) -> list:
    """
    This function read a file .txt and return\n
    an array of data.
    """
    data:list[str] = []
    data_employee:list[str] = []
    with open(path,'r') as file:
        data = file.readlines()
    file.close()
    for dt in data:
        data_employee.append(dt.replace("\n",""))
    return data_employee