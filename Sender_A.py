import socket
from encryption import encrypt, generate_otp_key

secret_word = b'secret'

host = socket.gethostname()
port_otp = 3500
port_data = 3501

# otp socket
socket_otp = socket.socket()
# data socket
socket_data = socket.socket()

# read file
try:
    file = 'Zelenskyy1.dat'
    with open(file, 'rb') as f:
        data_plaintext_bytes = f.read()

    # generate random otp
    otp_plaintext_bytes = generate_otp_key(len(data_plaintext_bytes))
    print(f'OTP generated ...')

    # encryption logic
    data_cipher_bytes = encrypt(data_plaintext_bytes, otp_plaintext_bytes)
    print(f'{file} encrypted ...')
    otp_cipher_bytes = encrypt(otp_plaintext_bytes, secret_word)
    print(f'OTP encrypted ...')

    try:
        # establish otp connection
        socket_otp.connect((host, port_otp))
        print(f'OTP connection established')

        socket_otp.sendall(otp_cipher_bytes)
        print(f'OTP sent')

        try:
            # establish data connection
            socket_data.connect((host, port_data))
            print(f'Data connection established')

            socket_data.sendall(data_cipher_bytes)
            print(f'Data from {file} sent')

        except socket.error as e:
            print(f"Socket error: {e}")

    except socket.error as e:
        print(f"Socket error: {e}")

except FileNotFoundError:
    print(f"Error: The file '{file}' was not found.")

finally:
    socket_otp.close()
    socket_data.close()
    print("Sockets closed.")
            