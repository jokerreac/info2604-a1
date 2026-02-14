##########################################################################

import socket #Import socket
try:
    s = socket.socket() #Create a socket object
    host = socket.gethostname() #Get local machinename
    port = 1345 #Reserve a port for your service
    
    s.connect((host, port)) #Bind to the port
    
    try: 
        file = 'text.txt'
        f = open(file,'rb')
        print(f'Sending {file}...')
        data = f.read(1024)
        while (data):
          print ('Sending data... ')
          s.sendall(data) # Use sendall() for reliability
          data = f.read(1024)
          
        f.close()
        print ("Done Sending...")
        s.shutdown(socket.SHUT_WR)# Inform the server that we are done sending data
        # Receive final confirmation from the server
        print('Server response:', s.recv(1024).decode('utf-8')) 

    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
        
except socket.error as e:
    print(f"Socket error: {e}")

finally:
    s.close()
    print("Socket closed.")