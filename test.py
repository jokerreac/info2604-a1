import random


def encrypt(plain_text, key):
    cipher_text = ''
    key_len = len(key)
    for i, char in enumerate(plain_text):
        cipher_text += chr((ord(char) + ord(key[i % key_len])) % 256)
    
    return cipher_text


def decrypt(cipher_text, key):
    plain_text = ''
    key_len = len(key)
    for i, char in enumerate(cipher_text):
        plain_text += chr((ord(char) - ord(key[i % key_len])) % 256)

    return plain_text


def generate_otp_key(length):
    otp = ''
    for i in range(length):
        otp += chr(random.randint(0, 255))
    
    return otp