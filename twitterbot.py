#twiiter bot using tweepy libary to obtain twitter api, 
import tweepy
from time import sleep
from credentials import *
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME
# This is hastag which Twitter bot will 
# search and retweet You can edit this with 
# any hastag .For example : '# javascript' 
QUERY = ' # anything'
# Twitter bot setting for liking tweets
LIKE = True
# bot setting for following users
FOLLOW =  True
# Twitter bot sleep time settings in seconds.  
# For example SLEEP_TIME = 300 means 5 minutes. 
# Please, use large delay if you are running bot  
# all the time so that your account does not 
# get banned. 

SLEEP_TIME = 300

#This is a sample file. you need to 
#edit this file. you need to get these
#details from your twitter app settings.
consumer_key = ''
consumer_secret = ''
acess_token = ''
aceess_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print("Twitter bot which retweets, likes tweets and follows users")
print("Bot Settings")
print("Like Tweets:", LIKE)
print("Follow Users:", FOLLOW)

for tweet in tweepy.Cursor(api.search, q = QUERY).items():
    try:
        print('\nTweet by: @ '+ tweet.user.screen_name)
        
        tweet.retweet() #retweets the tweet
        print('Retweeted the tweet')
        #favorite the tweet
        if LIKE:
            tweet.favorite()
            print('Favorited the tweet')
        #follow the user who tweeted
        # check that bot hasnt already following the user
        if FOLLOW:
            if not tweet.user.following:
                tweet.user.follow()
                print('Followed the user')
        sleep(SLEEP_TIME)
    
    except tweepy.TweepError as e:
        print('e.reason') #dont be dumb and spell things correctly and the program will work :D
    except StopIteration:
        break #ends the program after complete iteration. 