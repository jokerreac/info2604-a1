import socket
from encryption import decrypt

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
print(f'Receive is up and running - listening on ports {port_otp} and {port_data}')

while 1:
    # establish connection for OTP
    otp_recevied = []
    print(f'Waiting for OTP ...')
    otp_conn, addr = socket_otp.accept()
    while 1:
        otp_chunk = otp_conn.recv(1024)
        if not otp_chunk:
            break
        otp_recevied.append(otp_chunk)
    otp_cipher = b''.join(otp_recevied)
    print(f'OTP received')

    # establish connection for data
    data_received = []
    print(f'Waiting for data ...')
    data_conn, addr = socket_data.accept()
    while 1:
        data_chunk = data_conn.recv(1024)
        if not data_chunk:
            break
        data_received.append(data_chunk)
    data_cipher = b''.join(data_received)
    print(f'Data recived')

    # decryption Logic
    otp_plaintext = decrypt(otp_cipher, secret_word)
    data_plaintext = decrypt(data_cipher, otp_plaintext)

    with open('Zelenskyy2.dat', 'wb') as f:
        f.write(data_plaintext)
    
    otp_conn.close()
    data_conn.close()


  





