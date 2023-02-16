#rc4 stream cipher with lsfr and advanced permutation

import codecs

hex_to_char = codecs.getdecoder("hex_codec")
byte_to_int = codecs.getencoder("hex_codec")

def LFSR(plaintext, key):
    plaintext = hex_to_bin(plaintext)
    key = hex_to_bin(key)
    xor = int(plaintext, 2) ^ int(key, 2)
    xor = bin(xor)[2:].zfill(8)
    xor = xor[1:] + xor[0]
    return xor




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
    key = [ord(c) for c in key]
    plaintext = [ord(c) for c in plaintext]
    S = key_scheduling_algorithm(key)
    n = len(plaintext)
    key = pseudo_random_generation_algorithm(S, n)
    ciphertext = []
    for i in range(n):
        ciphertext.append(chr(plaintext[i] ^ key[i]))
    return "".join(ciphertext)

def main():
    key = "Key"
    plaintext = "Ujuro"
    ciphertext = rc4_convert(key, plaintext)
    print(ciphertext)
    decypertext = rc4_convert(key, ciphertext)
    print(decypertext)

if __name__ == "__main__":
    main()