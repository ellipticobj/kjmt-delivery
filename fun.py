import json

def readdatadict(filepath):
    '''
    made to read data from dat.json, potentially more uses in the future
    '''
    with open(filepath, 'r') as file:
        data = json.load(file)
    print(f"data read from file:\ndata: {data}\n file: ./{filepath}")
    return data

def dumpdatadict(filepath, data):
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
    data = readdatadict(filepath)
    data["client"] = updatedclientid
    return dumpdatadict(filepath, data)

def updatemanagerid(filepath, updatedmanagerid):
    '''
    allows users to update their manager channel id
    '''
    data = readdatadict(filepath)
    data["manager"] = updatedmanagerid
    return dumpdatadict(filepath, data)

# TODO make something to read token, ids