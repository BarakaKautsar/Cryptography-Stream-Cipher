#rc4 stream cipher with lsfr and advanced permutation

import codecs
import vigenereExtended as vigenereExt

hex_to_char = codecs.getdecoder("hex_codec")
byte_to_int = codecs.getencoder("hex_codec")

def xor_text(message, key):
    if type(message)!=list:
        message = [ord(c) for c in message]
    if type(key)!=list:
        key = [ord(c) for c in key]
    ciphertext = []
    for i in range(len(message)):
        ciphertext.append(chr(message[i] ^ key[i]))
    return "".join(ciphertext)
    


def xor_bits (bits):
    xor = 0
    for bit in bits:
        xor = xor ^ bit
    return xor

def LFSR(plaintext, key):
    register = [1 if bit =="1" else 0 for bit in key]
    keystream = []
    for i in range(len(plaintext)):
        temp = "0b"
        for _ in range (8):
            register.append(xor_bits(register))
            temp += str(register.pop(0))
        keystream.append(int(temp, 2))
    return keystream




def key_scheduling_algorithm(key):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

#modified PRGA with LFSR
def pseudo_random_generation_algorithm(S, n):
    i = 0
    j = 0
    key = []
    for k in range(n):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        key.append(S[(S[i] + S[j]) % 256])
    return key


def rc4_convert (key, plaintext):
    vig_key = key
    key = [ord(c) for c in key]
    plaintext = [ord(c) for c in plaintext]
    S = key_scheduling_algorithm(key)
    n = len(plaintext)
    key = pseudo_random_generation_algorithm(S, n)
    # vig_key = [chr(k) for k in key]
    ciphertext = [] 
    for i in range(n):
        ciphertext.append(plaintext[i] ^ key[i])
    ciphertext = xor_text(ciphertext, LFSR(plaintext, key))
    ciphertext = [ord(c) for c in ciphertext]
    vigenereExt_cipher = vigenereExt.encrypt(vig_key, vig_key)
    vigenereExt_cipher = [ord(c) for c in vigenereExt_cipher]
    #print(ciphertext)
    for i in range(len(ciphertext)):
        ciphertext[i] = chr(ciphertext[i] ^ vigenereExt_cipher[i % len(vigenereExt_cipher)])
    #ciphertext = xor_text(vigenereExt_cipher, ciphertext) 
    return ("".join(ciphertext))

def main():
    key = "raka"
    plaintext = "raka"
    ciphertext = rc4_convert(key, plaintext)
    print("ciphertext:" + ciphertext)
    decypertext = rc4_convert(key, ciphertext)
    print("decryptext:" + decypertext)
    # with open("logo.png", "rb") as save:
    #     cipher = rc4_convert(key, save.read().decode("latin-1"))

    # with open("logo_encrypted.txt", "wb") as save:
    #     save.write(cipher.encode("latin-1"))

    # with open ("logo_encrypted.txt", "rb") as save:
    #     plain = rc4_convert(key, save.read().decode("latin-1"))
    
    # with open("logo_decrypted.png", "wb") as save:
    #     save.write(plain.encode("latin-1"))

if __name__ == "__main__":
    main()