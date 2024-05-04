from cryptography.fernet import Fernet
import hashlib


def create_secret():
    keystring = input("enter key:"); 
    secr3t = getpass.getpass("enter secr3t:");
    print("original string: ", secr3t)
    hash_secr3t = fernet.encrypt(secr3t.encode("utf-8"))                                                             
    print("encrypted string: ", hash_secr3t)
    key_secr3t_manager[keystring] = hash_secr3t
    with open('keysecr3t.json', 'w', encoding='utf-8') as fp:
     json.dump(key_secr3t_manager, fp)
    print("secret stored hapyly")

def get_scret():

     keystring = input("enter key :")    
     with open('keysecr3t.json', 'r') as fp:
         key_secr3t_manager = json.load(fp)
     for key in key_secr3t_manager:
           if(key == keystring):
            value=key_secr3t_manager[keystring]
            value=fernet.decrypt(value)
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
