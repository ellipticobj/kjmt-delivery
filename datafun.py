import json, os, genfun

debug = False

'''
this is NO LONGER deprecated!!!
'''

def __fetchdata(filepath: str) -> dict[str, str]:
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
        if debug: print(f"data read from file: \ndata: {data}\n file: ./{filepath}")
        else: print("data read")
        return data
    except Exception as e:
        genfun.errormes(e)
        return {"": ""}

def fetchdatabyid(filepath: str, id: str) -> str:
    '''
    made to read data from dat.json, potentially more uses in the future
    '''
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
        if debug: print(f"data read from file by id: data: {data}\nid: {id}\ndata at id: {data[id]}\n file: ./{filepath}")
        else: print("data read by id")
        return data[id]
    except Exception as e:
        genfun.errormes(e)
        return ""

def moddatabyid(filepath: str, dataid, newd):
    '''
    allows user to modify data by its identifier, here just in case
    might change other dump functions to this
    '''
    
    data = __fetchdata(filepath)
    try:
        oldd = data[dataid]
        data[dataid] = newd
    except Exception as e:
        genfun.errormes(e)
        return 0
    if debug: print(f"data modified by id\ndata id: {dataid}\nchanges: {oldd} -> {newd}")
    else: print("data modified by id")
