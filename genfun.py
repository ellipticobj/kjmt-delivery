import datafun, profanity_check, re
from typing import Tuple

def errormes(e):
    print(f"error:\n{e}\nend. aw... :(")

def usrnameisvalid(username: str) -> Tuple[bool, str]:
    '''
    checks for validity of username
    '''
    if profanity_check.predict([username]):
        return False, "Username may contain offensive terms."
    if len(username) < 2 or len(username) > 24:
        return False, "Username must be between 2 and 24 characters"
    if not re.match(r'^\w+$', username):
        return False, "Username can only contain letters, numbers or underscores"
    return True, ""
