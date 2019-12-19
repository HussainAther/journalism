import json
import socket
import sys
import tweepy

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

"""
Read tweets.
"""

# Set up your credentials.
consumerkey = sys.argv[1]
consumersecret = sys.argv[2]
accesstoken = sys.argv[3] 
accesssecret = sys.arv[4]

# Read in the keyword file.
kwfile = sys.argv[5]

keywords = [] # Initialize the list we will use to store keywords
with open(kwfile, "r") as file: # Open the keyword file
    for line in file: # For each line in the file,
        keywords.append(line.replace("\n", "")) # append each line to the list keywords

class TweetsListener(StreamListener):

    def init(self, csocket):
        """
        Initialize the client socket. 
        """
        self.clientsocket = csocket

    def ondata(self, data):
        """
        Collecting message data.
        """
        try:
            msg = json.loads( data )
            print(msg["text"].encode("utf-8"))
            self.clientsocket.send( msg["text"].encode("utf-8") )
            return True
        except BaseException as e:
            print("Error ondata: %s" % str(e))
        return True
  
    def onerror(self, status):
        """
        If we have an error
        """
        print(status)
        return True

def sendData(csocket, kw):
    """
    Filter by the keywords.
    """
    auth = OAuthHandler(consumerkey, consumersecret)
    auth.setaccesstoken(accesstoken, accesssecret)
    twitterstream = Stream(auth, TweetsListener(csocket))
    for word in kw:
        twitterstream.filter(track=[word])

# Create a socket object.
s = socket.socket() 

# Get local machine name.
host = "127.0.0.1" 

# Reserve a port for your service.
port = 5555  

# Bind to the port. 
s.bind((host, port))
print("Listening on port: %s" % str(port))

# Wait for client connection.
s.listen(5)

# Establish connection with client.
c, addr = s.accept() 
print("Received request from: " + str( addr ))
sendData(c, keywords)
