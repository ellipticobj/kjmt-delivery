import json

def fetchdata(filepath):
    '''
    made to read data from dat.json, potentially more uses in the future
    '''
    with open(filepath, 'r') as file:
        data = json.load(file)
    print(f"data read from file:\ndata: {data}\n file: ./{filepath}")
    return data

def fetchdataid(filepath, id):
    '''
    made to read data from dat.json, potentially more uses in the future
    '''
    with open(filepath, 'r') as file:
        data = json.load(file)
    print(f"data read from file by id:data: {data}\nid: {id}\ndata at id: {data[id]}\n file: ./{filepath}")
    return data[id]

def dumpdata(filepath, data):
    '''
    made to allow users to change things like the client channel id or manager channel id, potentially more uses in the future
    '''
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"data dumped to file\ndata: {data}\nfile: ./{filepath}")
    return 0

def updateclientid(filepath, updatedclientid):
    '''
    allows users to update their client channel id
    '''
    data = fetchdata(filepath)
    data["client"] = updatedclientid
    return dumpdata(filepath, data)

def updatemanagerid(filepath, updatedmanagerid):
    '''
    allows users to update their manager channel id
    '''
    data = fetchdata(filepath)
    data["manager"] = updatedmanagerid
    return dumpdata(filepath, data)

def moddatabyid(filepath, dataid, newd):
    '''
    allows user to modify data by its identifier, here just in case
    might change other dump functions to this
    '''
    data = fetchdata(filepath)
    try:
        oldd = data[dataid]
        data[dataid] = newd
    except Exception as e:
        return e
    print(f"data modified by id\ndata id: {dataid}\nchanges: {oldd} -> {newd}")
