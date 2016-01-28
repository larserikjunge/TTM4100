import time
from socket import *

# Get the server hostname and port as command line arguments                    
host = "127.0.0.1" 
port = 12000 
timeout = 1 # in seconds
 
# Create UDP client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Set socket timeout as 1 second
clientSocket.settimeout(timeout)

# Sequence number of the ping message
ptime = 0  

# Ping for 10 times
while ptime < 10: 
    ptime += 1
    # Format the message to be sent as in the Lab description	
    sendTimeRaw = time.time() 
    sendTimeFormated = time.asctime()
    data = "Ping "+str(ptime)+": "+str(sendTimeFormated) 
    
    try:
	# Send the UDP packet with the ping message
	clientSocket.sendto(data,(host,port)) 
	# Receive the server response
 	serverResponse, address = clientSocket.recvfrom(4096) 
	# Record the "received time"
	receivedTimeRaw = time.time()
	reveivedTimeFormated = time.asctime()
	# Display the server response as an output
	print "Message from server: "+serverResponse+"\n"



	# Round trip time is the difference between sent and received time
	roundTripTime = str(receivedTimeRaw-sendTimeRaw)
	print "Round trip time: "+roundTripTime+"\n\n"
        
    except:
        # Server does not response
	# Assume the packet is lost
	print "======================================================"
        print "Request timed out during Ping "+str(ptime)+"."
	print "======================================================\n"
        continue

# Close the client socket
clientSocket.close()
 
