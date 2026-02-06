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

    
plain_text = 'Hello World!'
key = 'why ALl the SaD faceS?'

cipher = encrypt(plain_text, key)
print(cipher)

plain = decrypt(cipher, key)
print(plain)