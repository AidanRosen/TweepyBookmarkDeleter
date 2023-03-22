import tweepy
import webbrowser


oauth2_user_handler = tweepy.OAuth2UserHandler(
    client_id="c2habTlfY2E2UnFxZkZBWmhkRzQ6MTpjaQ",
    redirect_uri="https://127.0.0.1",
    scope=["bookmark.read", "bookmark.write",
        "tweet.read","users.read"],
    # Client Secret is only necessary if using a confidential client
    client_secret="TYUYOyHgTl9u-tNBHNwOSz8TPhgP92XHEUnFxV0MDmSM6oz4ZG"
)



webbrowser.open(oauth2_user_handler.get_authorization_url(),new=1);


verifier = input("Enter whole callback URL: ")

 
accessToken = oauth2_user_handler.fetch_token(verifier)
#It turns out I still need to repeatedly authorize, but maybe not if I dothat dotenv stuff...

#print("The returned access token is ", accessToken, "\n\n\n the data type of accessToken is: ", type(accessToken), "\n\n\n Attempting to use subscript notation to get the access_token string: ", accessToken['access_token'])
#Eureka! The above works for fetching the access_token value! I can use that now instead of copy-pasting all the time omg 


#accessCopy = input("Copy paste the access token here \n >") #<-- I can automate this part in the near future to reduce the hassle of this 

client = tweepy.Client(accessToken['access_token']) #Interesting. When I copy paste directly, the next print statement STILL shows none, but the get_bookmarks code runs fine

#Lesson I learned: the NUANCE of the documentation was that it used a raw string, and I had the intuition that I was NOT using a string because I found out I was inputting a whole token data structure 
#^^^ determined by printing the output for each token so I could know exactly what I was printing 


#print("The client access token is ", client.access_token) #How interesting. IT shows that the access token is "none" despite following the steps 
#print("The data type of the access token is ", type(client.access_token)) #important to detect if it is a dictionary or not <-- the previosu print statement follows the structure of a dictionary

#print("Attempting to print the client on its own ", client) #Maybe I can use subscript access here? Is get_Bookmarks() a dictionary?

#print("Attempting to print the access_token key value: ", client.access_token['access_token']) #Do double vs single quotes matter? Trying to copy exactly what was printed
#The above is telling me the object is NOT a dictionary and is actually a noneType object, so it can't be accessed with subscript notation.
"""
IMPORTANT! It's not the client that has the access token I'm trying to copy, it's the accessToken variable! That's the thing I copy-paste from in the terminal <-- important to be aware of all variables. I need the data type of accessToken


"""



#print("The access token attribute within the access_token is ", client.access_token.access_token)    It seems the client access token doesn't have an attribute called access token... how do you extract that info then? Bizarre 

"""
tweets = client.get_bookmarks(expansions=None, #I need the access token! <-- learned this from reading the documentation for type error!
    tweet_fields=None,
    user_fields=None,
    media_fields=None) #I want to JUST fetch tweet IDs. How?
    
     #get the responses 
 """

#tweets = response.data #What does thie MEAN? According to the documentation, .data is a 


#print("The data type of tweets is ", type(response)) #This is a problematic line of code because some of the python tweepy types are unhasheable... ugh
#Strategy: comment so that only individual lines happen in sequence to isolate the glitchy line 



#Now I'll begin testing the id detection powers 

#print("Now printing the data type of tweets and they're content\n\n\n")

#for i in tweets: #to see if there are more lists of ids inside
 #   print("The data type is: ", type(i),"\n\n") #There are TWO lists. I wonder if the second list has more ids. It goes list, dict, list, dict.
  #  print(i)

#print("The data type of tweets is ", type(tweets), "\n\n\n")

#print("Attempting to post the twitter id list from the responses: ", tweets[0]) #<-- works! The list appears to contain tweet objects within, so I need to parse through the list within the first element of the bookmarks list

input("\n\nContinue?\n\n\n\n")





#What do I know? tweets[0] is a list. I need to know what kind of elements are stored so that I can fetch the tweet ID: (doing for each tweet so that there are no discrepancies

deleting = True 

while deleting == True:

    tweets = client.get_bookmarks(expansions=None, #I need the access token! <-- learned this from reading the documentation for type error!
    tweet_fields=None,
    user_fields=None,
    media_fields=None, max_results = 100) #Need this block to be here so that it always resets 
    
    print("Deleting ", len(tweets[0]) , " bookmarks\n")
    check = input("\nContinue? y/n \n")


    if check == "y": #I could represent this with a flowchart
        
        
        if len(tweets[0]) < 33:
            length = len(tweets[0])
            
        else:
            length = 33
            
        for i in range(0, length): #using indexes to cycle through the list rather than doing for element <-- so that I can use numbers and not big long prints 
    #print("The data type of element[",i,"] is : ", type(tweets[0][i])) #A nested list 
    #print("The tweet id of the tweet is: ", tweets[0][i].id)
    #print("\n\n")
            #client.remove_bookmark(tweet_id=tweets[0][i].id)
            print("Removing tweet @ id: ", tweets[0][i].id, "\n\n") #this counts as a request I think(?) Maybe not because the tweets are already saved in my array...
            
            
    elif check == "n":
        deleting = False
        
print("\n\n\n Exiting service")
    
#Result: good, the id fetching works. Now I just need a way to bump the size from 95 to 600 and then start deleting after using dewey. <-- does increasing the size require pagination token? What about media fields?
#NExt time, I should keep logs by date and time in like a text file or something. None fo these comments are in chronological order. Oh well. 

#What did this tell me? All the elements in the list are of the type tweet so I should be able to grab the id from each. Why only 95 elements though? Seems so low 

"""
for tweet in tweets: #for each key print the key, but it seems to be printing values with long, long lists UNLESS the key is the id and value is the media...
   
   print(tweet) #if its a dictionary, this would print the key... I don't think it is a dicitonary though...
   print("\n\n\nThis tweets type is: ", type(tweet))
   #This SHOULD print all the ids <-- following the tutorials syntax with the {} <-- what is a {} for? Looks like a dictionary <-- if this works, use the same syntax for access_token
   print("\n") #For formatting and ease of reading <-- had to move up here to avoid unexpected indent
    #But also, it says the object is a list --> I need to know what position the id is stored in so I can access it every time --> print the type of the tweet!
    
    
    
    #I'm trying to EXACTLY follow the tutorial with the printf <-- submit and do it exactly, duh. Sounds simple. Note: it doesn't follow dictionary syntax for accessing keys Result: 
    
    
    
    #Using print effectively! By printing each tweet I can find out what the error means when it says the tweet object is a list <-- a list as the value of each dictionary key?
    
    
"""    
    
"""

Notes: how do I get JUST tweet IDs? <-- using the list 

How do I get more than just 95 results? Documentation says it goes up to 800...



FUTURE: adapt reddit saved to csv to save likes to a spreadsheet and finally have all my saved stuff archived 

"""
