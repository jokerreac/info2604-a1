# STUDENT ID : 816041392

import random

# Extended Vigenère Cipher for encrpytion and decryption
def encrypt(plain_text, key):
    cipher_text = []
    key_len = len(key)
    for i, byte_val in enumerate(plain_text):
        cipher_text.append((byte_val + key[i % key_len]) % 256)
    
    return bytes(cipher_text)


def decrypt(cipher_text, key):
    plain_text = []
    key_len = len(key)
    for i, byte_val in enumerate(cipher_text):
        plain_text.append((byte_val - key[i % key_len]) % 256)

    return bytes(plain_text)

# Random OTP generation
def generate_otp_key(length):
    otp = []
    for i in range(length):
        otp.append(random.randint(0, 255))
    
    return bytes(otp)