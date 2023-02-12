
#Array of int from 0..255
S = [i for i in range(256)]

#Key Array of 256
K = [0 for i in range(256)]

#Key Scheduling Algorithm
def KSA(key, S):
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    
#Pseudo-Random Generation Algorithm
def PRGA():
    i = 0
    j = 0
    for i in range(256):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K

#Encryption
def encrypt(key, plaintext):
    key = [ord(c) for c in key]
    KSA(key, S)
    keystream = PRGA()
    return ''.join(chr(ord(c) ^ next(keystream)) for c in plaintext)

#Decryption
def decrypt(key, ciphertext):
    key = [ord(c) for c in key]
    KSA(key, S)
    keystream = PRGA()
    return ''.join(chr(ord(c) ^ next(keystream)) for c in ciphertext)

#Main
def main():
    key = "Key"
    plaintext = "Plaintext"
    ciphertext = encrypt(key, plaintext)
    print("Ciphertext: ", ciphertext)
    print("Decrypted: ", decrypt(key, ciphertext))

if __name__ == "__main__":
    main()