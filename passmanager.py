from cryptography.fernet import Fernet
import hashlib
import getpass
import json , codecs
key_secr3t_manager = {}
key = Fernet.generate_key()
fernet = Fernet(key)

def create_secret():
    keystring = input("enter key:");
    secr3t = getpass.getpass("enter secr3t:");
    print("original string: ", secr3t)
    hash_secr3t = fernet.encrypt(secr3t.encode())
    print("encrypted string: ", hash_secr3t)
    key_secr3t_manager[keystring] = hash_secr3t
    with open('keysecr3t.json', 'w') as fp:
        try:
         json.dump(key_secr3t_manager, codecs.getwriter('utf-8')(fp), ensure_ascii=False)
        except UnicodeEncodeError:
            print ("testing")
            pass

    print("secret stored hapyly")

def get_scret():
    keystring = input("enter key :")
    with open('keysecr3t.json', 'r') as fp:
        key_secr3t_manager = json.load(fp)
    for key in key_secr3t_manager:
        if(key == keystring):
            value=key_secr3t_manager[keystring]
            value=fernet.decrypt(value).decode()
            #.decode("utf-8")
            print (value)
            break
            #hash_secr3t = hashlib.sha256(secr3t.encode()).hexdigest()

def main():
    while True:
        choice = input("enter 1 to create a secret, 2 to get existing secret, or 0 to exit: ")
        if choice == "1":
            create_secret()
        elif choice == "2":
            get_scret()
        elif choice == "0":
            break
        else:
            print("invalid choice")

if __name__ == "__main__":
    main()