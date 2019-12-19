import cPickle
import os
import twitter 
 
# Usage:
# $ # setup CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET
# as environment variables
# $ python get_data.py  # downloads friend and follower data to ./data

# Errors seen at runtime:
# raise URLError(err)
# urllib2.URLError: <urlopen error [Errno 104] Connection reset by peer>

DATA_DIR = "data/twitter"  # storage directory for friend/follower data

# List of screen names that we"ll want to analyze.
screennames = ["science_ari", "shussainather", "laragstreiff", 
                "scatter_cushion", "jessekathan", "jackjlee",
                "erinmalsbury", "joetting13", "jonathanwosen",
                "heysmartash"]

def get_filenames(sn):
    """
    Build the friends and followers filenames.
    """
    return os.path.join(DATA_DIR, 
                        "%s.friends.pickle" % (sn)), 
                        os.path.join(DATA_DIR, 
                        "%s.followers.pickle" % (sn))

if __name__ == "__main__":
    """
    Get the tweets and information.
    """
    t = twitter.Api(ckey=os.getenv("CONSUMER_KEY"),
                    csecret=os.getenv("CONSUMER_SECRET"),
                    atk=os.getenv("ACCESS_TOKEN_KEY"),
                    ats=os.getenv("ACCESS_TOKEN_SECRET"))
    print(t.VerifyCredentials())
    print("Downloading friends and followers for:", screennames)
    for sn in screennames:
        fr_filename, fo_filename = get_filenames(sn)
        print "Checking for:", fr_filename, fo_filename
        if not os.path.exists(fr_filename):
            print "Getting friends for", sn
            fr = t.GetFriends(user=sn)
            cPickle.dump(fr, open(fr_filename, "w"), protocol=2)
        if not os.path.exists(fo_filename):
            print "Getting followers for", sn
            fo = t.GetFollowers(user=sn)
            cPickle.dump(fo, open(fo_filename, "w"), protocol=2)
