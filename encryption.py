import random


def encrypt(plain_text, key):
    cipher_text = b'' 
    key_len = len(key)
    for i, byte_val in enumerate(plain_text):
        cipher_text += bytes([(byte_val + key[i % key_len]) % 256])
    
    return cipher_text


def decrypt(cipher_text, key):
    plain_text = b'' 
    key_len = len(key)
    for i, byte_val in enumerate(cipher_text):
        plain_text += bytes([(byte_val - key[i % key_len]) % 256])

    return plain_text


def generate_otp_key(length):
    otp = b''
    for i in range(length):
        otp += bytes([random.randint(0, 255)])
    
    return otp