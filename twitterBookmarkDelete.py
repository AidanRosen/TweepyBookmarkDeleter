import math

import tweepy

# These are actual credentials; don't expose them!!
CONSUMER_KEY = "LCBWuRglofveFeKBApiPMTANb"
CONSUMER_SECRET = "GJCIyq49TXqA5vLfXE1VYsX1LBGwCwQ2eDf4KAXLfLYmWNkoAJ"
ACCESS_TOKEN = "1434174764998750208-ybKV1sCifp6WYUoGEMzOkuPaX5sWA4"
ACCESS_TOKEN_SECRET = "RvZvDWZxqHrPOjfAxDOtiFG7F3vuYQgLYnoaoQqMHHAac"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAB%2B4ewEAAAAA%2F84JUZI4p4wtyoFC8Kfw%2Brvvvxo%3Dvr4fEVoXl5qShKiKMqvs2SMFx2cXy4AM0QfJ1FErcuj0GkvuMV"

#auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#api = tweepy.API(auth)

TWEETS_PER_REQUEST = 50  # 200 is the max, using 50 to monitor it 
NUMBER_OF_TWEETS = 0  # total number of tweets you have
iterations = 615 #deleting groups before using Dewey again

"""

#I need to delete the for statement below in order to keep the script from deleting ALL my bookmarks 
for i in range(1, iterations + 1):  # +1 to include the last batch
    print(f'Getting batch of {i * TWEETS_PER_REQUEST}..')
    my_tweets = api.user_timeline(count=TWEETS_PER_REQUEST) #HERE is where I edit to bookmarks to delete bookmarks, note the function returns a dictionary
    #Note, the above also defines a variable that contains the dictionary 
    
    
    
    #I need to put a limit on this for loop to limit the amount of deletions to 600, not the total 800
    for tweet in my_tweets: #for each bookmark in bookmarksList, delete them <-- multiplication as a function? Same wording, for [first arg] get/total up [second arg] 
        print(f'Deleting tweet {tweet.id}..')
        api.destroy_status(tweet.id)
        
        
"""



#sauce code: https://gist.github.com/JulianHysi/1acf537d25f42f8c9b0526b70b2c7752 
#Documentation https://docs.tweepy.org/en/stable/client.html 




#Notes on dealing with the dictionary:
# I can for-loop parse through the dictionary of all my bookmarks, BUT I need a way to get the tweet id from each tweet element of the dictionary 

#                 Ie for tweet in dict: remove.bookmark(tweet.SYNTAXFORTWEETID)


# I need a way to stop at the 615th entry... <-- Why I wanted a list in the first place 

#My loop code 

"""

i = 0

for tweet in array:
   if i < 615: 
    print(f'Deleting tweet ' + i)
    Client.remove_bookmark(tweet.id)
   else:
      print(f'Skipping delete, limit reached')    
      
      
      
      #for now, why don't I just print the dictionary to see what I'm looking at 
      
      """
      
      
      


api = tweepy.Client(bearer_token = BEARER_TOKEN, consumer_key = CONSUMER_KEY, consumer_secret = CONSUMER_SECRET, access_token = ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)


myBookmarks = api.get_bookmarks()

"""
#print(myBookmarks) lame and inefficient to read 600 items

for key,value in myBookmarks.items():
	print(key, ':', value, "\n")
    #cool and epic display. I hope the line break character works 
    
"""
    
    
print("> Success authenticating")