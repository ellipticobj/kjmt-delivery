from cryptography.fernet import Fernet

KEYPATH = "./.key"
envcrypted = False

try:
    with open(KEYPATH, 'wr') as KEYF:
        key = KEYF.read()
        print(f"read key from {KEYPATH}")
        print(f"assuming .env is encrypted with keyval {key}")
except FileNotFoundError:
    print(f"{KEYPATH} not found, making new file")
    print("assuming .env is not encoded")
    

key = Fernet.generate_key()
