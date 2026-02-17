# STUDENT ID : 816041392

import socket
from encryption import decrypt

# pre-shared secret word
secret_word = b'secret'

host = socket.gethostname()
port_otp = 3500
port_data = 3501

# otp socket
socket_otp = socket.socket()
socket_otp.bind((host, port_otp))

# data socket
socket_data = socket.socket()
socket_data.bind((host, port_data))

# wait for sender
socket_otp.listen()
socket_data.listen()
print(f'> Receiver is up and running ...\n')

# establish connection for OTP
otp_recevied = []
print(f'Waiting for OTP on port#{port_otp} ...')
otp_conn, addr = socket_otp.accept()
while 1:
    otp_chunk = otp_conn.recv(1024)
    if not otp_chunk:
        break
    otp_recevied.append(otp_chunk)
otp_cipher = b''.join(otp_recevied)
print(f'> OTP received!\n')

# establish connection for data
data_received = []
print(f'Waiting for data on port#{port_data} ...')
data_conn, addr = socket_data.accept()
while 1:
    data_chunk = data_conn.recv(1024)
    if not data_chunk:
        break
    data_received.append(data_chunk)
data_cipher = b''.join(data_received)
print(f'> Data received!\n')

# save cipher to local storage
file = 'Zelenskyy2.dat'
with open(file, 'wb') as f:
    f.write(data_cipher)
print(f'> {file} saved successfully!')

# decrypt otp and data cipher
otp_plaintext = decrypt(otp_cipher, secret_word)
print(f'> OTP decrypted successfully!')
data_plaintext = decrypt(data_cipher, otp_plaintext)
print(f'> {file} decrypted successfully!\n')

# print final decoded output
print(f'========== Decrypted Message ==========')
print(f'{data_plaintext.decode('utf-8')}')
print(f'=======================================\n')

otp_conn.close()    
data_conn.close()
socket_otp.close()
socket_data.close()
print(f'> Connections closed!')
print(f'> Receiver terminated!')