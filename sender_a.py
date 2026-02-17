# STUDENT ID : 816041392

import socket
from encryption import encrypt, generate_otp_key

# pre-shared secret word
secret_word = b'secret'

host = socket.gethostname()
port_otp = 3500
port_data = 3501

# otp socket
socket_otp = socket.socket()
# data socket
socket_data = socket.socket()

print(f'> Sender is up and running ...\n')

file = 'Zelenskyy1.dat'
print(f'Reading {file} ...')

try:
    # read file
    with open(file, 'rb') as f:
        data_plaintext = f.read()
    print(f'> {file} read successfully!\n')

    # generate random otp
    otp_plaintext = generate_otp_key(len(data_plaintext))
    print(f'> OTP generated!')

    # encrypt data and otp
    data_cipher = encrypt(data_plaintext, otp_plaintext)
    print(f'> {file} encrypted successfully!')
    otp_cipher = encrypt(otp_plaintext, secret_word)
    print(f'> OTP encrypted successfully!\n')

    try:
        # establish otp connection
        socket_otp.connect((host, port_otp))
        print(f'OTP connection established on port#{port_otp} ...')
        socket_otp.sendall(otp_cipher)
        print(f'> OTP sent successfully!\n')

        try:
            # establish data connection
            socket_data.connect((host, port_data))
            print(f'Data connection established on port#{port_data} ...')
            socket_data.sendall(data_cipher)
            print(f'> Encrypted {file} sent successfully!\n')

        except socket.error as e:
            print(f"Socket error: {e}")

    except socket.error as e:
        print(f"Socket error: {e}")

except FileNotFoundError:
    print(f"Error: The file '{file}' was not found.")

finally:
    socket_otp.close()
    socket_data.close()
    print(f'> Connections closed!')
    print(f'> Sender terminated!')
            