import json, os, genfun
from typing import Any

debug = False

'''
this is NO LONGER deprecated!!!
'''

def __loaddata(filepath: str) -> dict[str, Any]:
    '''
    loads an entire json file as a dictionary
    '''
    with open(filepath, 'r') as file:
        return json.load(file)

def loaddata(filepath: str, dataid: str = "", findrecent=True) -> str:
    '''
    loads data at dataid in a json file, or the data with the largest key if findrecent is True
    '''
    data = __loaddata(filepath)
    if findrecent:
        return data[max(data.keys())]
    else:
        return data[dataid]

def dumpdata(filepath, data):
    '''
    overwrites the entire json file with the new data
    '''
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)

def moddata(filepath: str, dataid, newdata):
    '''
    changes the data at dataid in the json file
    '''
    data = __loaddata(filepath)
    data[dataid] = newdata
    dumpdata(filepath, newdata)

    
