import json
import os
import pickle
import twitter 

""" 
Get friends and followers from Twitter.
This example uses the UCSC Science Communication students 
from the class of 2020 as an example. 

Usage:
$ # setup CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET
as environment variables
$ python get_data.py  
"""

# Storage directory for data
datadir = "data/twitter"
 
# List of the UCSC SciCom students that we'll want to analyze
screennames = ["science_ari", "shussainather", "laragstreiff", 
                "scatter_cushion", "jessekathan", "jackjlee",
                "erinmalsbury", "joetting13", "jonathanwosen",
                "heysmartash"]

CONSUMER_KEY = "OKCz6x0AWToiTM8ZmQ2uqYH5u"
CONSUMER_SECRET = "fTbIoojwok3oymzFGZQ0uv7OoXZFyA29GQTEbpi2XjH3oxG662"
ACCESS_TOKEN_KEY = "1149121881217359872-EnxJZ67rtoxs3iXqJeasFGduCa6WDz"
ACCESS_TOKEN_SECRET = "koXMF3a1Uy15ZBawtWiLE7WTluW5pd24uNfhuHmy8pWvO"

if __name__ == "__main__":
    """
    Get the tweets and information.
    """
    t = twitter.Api(consumer_key = CONSUMER_KEY,
                    consumer_secret = CONSUMER_SECRET,
                    access_token_key = ACCESS_TOKEN_KEY,
                    access_token_secret = ACCESS_TOKEN_SECRET)
    for sn in ["shussainather"]:
        """
        For each user, get the followers and tweets and save them
        to output pickle and JSON files.
        """
        # Get the follower information.
        fof = t.GetFollowers(screen_name = sn)
        print(fof)
        fo = datadir + "/" + sn + ".followers.pickle" 
        with open(fo, "w") as fofpickle:
            pickle.dump(fof, fofpickle, protocol = 2)
        with open(fo, "r") as fofpickle:
            with open(fo.replace(".pickle", ".json"), "w") as fofjson:
                fofdata = pickle.load(fofpickle)
                json.dump(fofdata, fofjson)      

        # Get the user's timeline with the ten most recent tweets.
        timeline = t.GetUserTimeline(screen_name=sn, count=500)
        tweets = [i.AsDict() for i in timeline]
        with open(datadir + "/" + sn + ".tweets.json", "w") as tweetsjson:
            json.dump(tweets, tweetsjson) # Store the informtion in a JSON. 
