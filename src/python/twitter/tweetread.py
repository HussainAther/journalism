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
