from cryptography.fernet import Fernet
 
 

def encrypt(message):
    
    key = b'BweMjIwfudLhwk9GPNAKwywXrOOoCB6_YQaxcZvsES4='#Fernet.generate_key()
 
    fernet = Fernet(key)
 

    encMessage = fernet.encrypt(message.encode())
 
    # print("original string: ", message)
    # print("encrypted string: ", encMessage)
    return encMessage

def decrypt(encMessage): 
    key = b'BweMjIwfudLhwk9GPNAKwywXrOOoCB6_YQaxcZvsES4='#Fernet.generate_key()
 
    fernet = Fernet(key)



    decMessage = fernet.decrypt(encMessage).decode()
 
    # print("decrypted string: ", decMessage)
    return decMessage
