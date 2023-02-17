def plaintext_file_read_binary(filename):
    with open(filename, "rb") as f:
        plaintext = f.read()
    return plaintext

def generateKeySting(string,key):
    key = list(key)
    keyString = []
    for i in range (len(string)):
        keyString.append(key[i % len(key)])
    return("".join(keyString))

def encrypt(plaintext,key):
    ciphertext = []
    keyString = generateKeySting(plaintext,key)
    plaintext = str(plaintext)
    for i in range (len(plaintext)):
        x = ((ord(plaintext[i])+ord(keyString[i])) % 256) 
        ciphertext.append(chr(x))
    return("".join(ciphertext))

def decrypt (ciphertext,key):
    plaintext = []
    keyString = generateKeySting(ciphertext,key)
    for i in range(len(ciphertext)):
        x = ((ord(ciphertext[i])-ord(keyString[i])+256) % 256)
        plaintext.append(chr(x))
    return("".join(plaintext))