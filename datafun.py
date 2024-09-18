import json, os, genfun

debug = False

'''
this is NO LONGER deprecated!!!
'''

def __loaddata(filepath: str) -> dict[str, str]:
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def loaddata(filepath: str, dataid: str = "", findrecent=True) -> str:
    '''
    made to read data from dat.json, potentially more uses in the future
    '''
    data = __loaddata(filepath)
    if findrecent:
        return data[max(data.keys())]
    else:
        return data[dataid]

def dumpdata(filepath, data):
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)

def moddata(filepath: str, dataid, newd):
    '''
    allows user to modify data by its identifier, here just in case
    might change other dump functions to this
    '''
    data = __loaddata(filepath)
    data[dataid] = newd
    dumpdata(filepath, newd)

    
