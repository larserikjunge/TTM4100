from socket import *    


# Create a TCP server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 6789

# Bind the socket to server address and server port
serverSocket.bind(('', serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)


while True:
	print 'Ready to serve...'
	
	# Set up a new connection from the client
	connectionSocket, addr = serverSocket.accept()
	
	try:
		# Receives the request message from the client
		message =  connectionSocket.recv(1024)
		# Extract the path from the message
		filepath = message.split()[1]
		
		# Read the file into a buffer
		f = open(filepath[1:])
		outputdata = f.read()
		
		# Send the HTTP response header line to the connection socket
		connectionSocket.send("HTTP/1.1 200 OK \r\n\r\n")
 		
		# Send the requested file to the connection socket
		for i in range(0, len(outputdata)):  
			connectionSocket.send(outputdata[i])
		connectionSocket.send("\r\n")
		
		# Close the client connection socket
		connectionSocket.close()

	except IOError:
		# Send HTTP response mesage for file not found
		connectionSocket.send("HTTP/1.1 404 Not Found \r\n\r\n")
		connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
		
		connectionSocket.close()	

serverSocket.close()  

