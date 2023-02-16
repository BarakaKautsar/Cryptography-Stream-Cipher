

#Key Scheduling Algorithm
def KSA(key):

    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S
    
#Pseudo-Random Generation Algorithm generate key in string
def PRGA(S, n):
    i = 0
    j = 0
    key = []
    for k in range(n):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        key.append(S[(S[i] + S[j]) % 256])
    return key




#Encryption
def encrypt(key, plaintext):
    key = [ord(c) for c in key]
    plaintext = [ord(c) for c in plaintext]
    S = KSA(key)
    n = len(plaintext)
    key = PRGA(S, n)
    ciphertext = []
    for i in range(n):
        ciphertext.append(str(hex(plaintext[i] ^ key[i])))
    return "".join(ciphertext)

#Decryption
def decrypt(key, ciphertext):
    key = [ord(c) for c in key]
    ciphertext = [int(c, 16) for c in ciphertext.split()]
    S = KSA(key)
    n = len(ciphertext)
    key = PRGA(S, n)
    plaintext = []
    for i in range(n):
        plaintext.append(chr(ciphertext[i] ^ key[i]))
    return "".join(plaintext)


#Main
def main():
    key = "Key"
    plaintext = "Plaintext"
    ciphertext = encrypt(key, plaintext)
    print(ciphertext)
    print(decrypt(key, ciphertext))

if __name__ == "__main__":
    main()