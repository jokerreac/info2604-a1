##########################################################################

import socket #Import socket module
s = socket.socket() #Create a socket object
host = socket.gethostname() #Get local machine name
port = 1345 #Reserve a port for your service
s.bind((host, port)) #Bind to the port
s.listen(5) #Now wait for client connection
print ("Server listening on port", port)
while True:
  c, addr = s.accept() #Establish connection
  print ("Got connection from", addr)
  print ("Receiving...")
  
  with open('text1.txt','wb') as f:
   while True:
     data = c.recv(1024)
     if not data:
       break #Break the loop when data stops coming
     f.write(data)
     
  print ("Finish Receiving...")
  c.send(b"Thank you for connecting!");#Send bytes (Python 3 requires bytes
  c.close() #Close the connection
