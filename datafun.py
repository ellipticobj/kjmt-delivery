import json, os, genfun

debug = False

'''
this is NO LONGER deprecated!!!
'''

def __fetchdata(filepath: str) -> dict[str, str]:
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def fetchdata(filepath: str, id: str = "", findrecent=True) -> str:
    '''
    made to read data from dat.json, potentially more uses in the future
    '''
    data = __fetchdata(filepath)
    if findrecent:
        return data[max(data.keys())]
    else:
        return data[id]

def moddata(filepath: str, dataid, newd):
    '''
    allows user to modify data by its identifier, here just in case
    might change other dump functions to this
    '''
    data = __fetchdata(filepath)
    oldd = data[dataid]
    data[dataid] = newd
    with open(filepath, "w") as file:
        json.dump(newd, file, indent=4)
    
