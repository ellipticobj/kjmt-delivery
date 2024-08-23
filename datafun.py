import json, os, genfun

debug = False

def fetchdata(filepath: str):
    '''
    made to read data from dat.json, potentially more uses in the future
    '''
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
        if debug: print(f"data read from file: \ndata: {data}\n file: ./{filepath}")
        else: print("data read")
        return data
    except Exception as e:
        genfun.errormes(e)
        return 0

def fetchdatabyid(filepath: str, id: str):
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
        return 0

def dumpdata(filepath: str, data):
    '''
    made to allow users to change things like the client channel id or manager channel id, potentially more uses in the future
    '''
    try:
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
        if debug: print(f"data dumped to file\ndata: {data}\nfile: ./{filepath}")
        else: print(f"data dumped to {file}")
        return 0
    except Exception as e:
        genfun.errormes(e)
        return 0

def updateclientid(filepath, updatedclientid):
    '''
    allows users to update their client channel id
    '''
    try:
        data = fetchdata(filepath)
        data["client"] = updatedclientid
        return dumpdata(filepath, data)
    except Exception as e:
        genfun.errormes(e)
        return 0

def updatemanagerid(filepath: str, updatedmanagerid):
    '''
    allows users to update their manager channel id
    '''
    try:
        data = fetchdata(filepath)
        data["manager"] = updatedmanagerid
        return dumpdata(filepath, data)
    except Exception as e:
        genfun.errormes(e)
        return 0

def moddatabyid(filepath: str, dataid, newd):
    '''
    allows user to modify data by its identifier, here just in case
    might change other dump functions to this
    '''
    
    data = fetchdata(filepath)
    try:
        oldd = data[dataid]
        data[dataid] = newd
    except Exception as e:
        genfun.errormes(e)
        return 0
    if debug: print(f"data modified by id\ndata id: {dataid}\nchanges: {oldd} -> {newd}")
    else: print("data modified by id")
