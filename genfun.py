import datafun

def errormes(e):
    print(f"error:\n{e}\nend. aw... :(")
    
def checkmostrecent(path: str) -> str:
    try:
        with open(f"{path}/list.json"):
            typeid = datafun.fetchdata
    except FileNotFoundError:
        print(f"list.json in {path} does not exist :(")
    return f"{typeid}"