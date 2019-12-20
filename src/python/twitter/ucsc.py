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

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN_KEY = os.getenv("ACCESS_TOKEN_KEY")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

def getfilenames(sn):
    """
    Build the friends and followers filenames.
    """
    return os.path.join(datadir, "%s.friends.pickle" % (sn)), os.path.join(datadir, "%s.followers.pickle" % (sn))

if __name__ == "__main__":
    """
    Get the tweets and information.
    """
    t = twitter.Api(consumer_key = CONSUMER_KEY,
                    consumer_secret = CONSUMER_SECRET,
                    access_token_key = ACCESS_TOKEN_KEY,
                    access_token_secret = ACCESS_TOKEN_SECRET)
    for sn in screennames:
        """
        For each user, get the friends, followers and tweets and save them
        to output pickle and JSON files.
        """
        fr, fo = getfilenames(sn)

        # Get the friends infromation.
	frf = t.GetFriends(user_id = sn)
        with open(fr, "w") as frfpickle:
            pickle.dump(frf, frfpickle, protocol = 2) # Write out to a pickle file.
        with open(fr, "r") as frfpickle: # Open the pickle file.
            with open(fr.replace(".pickle", ".json"), "w") as frfjson: 
                frfdata = pickle.load(frfpickle) # Get the pickle file's contents.
                json.dump(frfdata, frfjson) # Write to a JSON file.
   
        # Get the follower information.
        fof = t.GetFollowers(user_id = sn)
        with open(fo, "w") as fofpickle:
            pickle.dump(fof, fofpickle, protocol = 2)
        with open(fo, "r") as fofpickle:
            with open(fo.replace(".pickle", ".json"), "w") as fofjson:
                fofdata = pickle.load(fofpickle)
                json.dump(fofdata, fofjson)      

        # Get the user's timeline with the ten most recent tweets.
        timeline = t.GetUserTimeline(screen_name=sn, count=10)
        tweets = [i.AsDict() for i in timeline]
        with open(datadir + "/" + sn + ".tweets.json", "w") as tweetsjson:
            json.dump(tweets, tweetsjson) 
