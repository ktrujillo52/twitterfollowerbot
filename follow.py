#!/usr/bin/python
import tweepy #https://github.com/tweepy/tweepy
import time
import re

#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

#Keywords
pattern = ['word1', 'word2', 'word3', 'word4', 'word5']

def get_all_tweets(screen_name):
    count = 0
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    #get all followers
    ids = []
    for page in tweepy.Cursor(api.followers_ids, screen_name).pages():
        ids.extend(page)
        time.sleep(60)
    #grab user bio
    for i in ids:
        test = api.lookup_users(user_ids=[i])
        for user in test:
            bio = user.description
            r = bio.split()
            print bio
            do = 0
            for k in r:
                if k == pattern[0] or k == pattern[1] or k == pattern[2] or k == pattern[3] or k == pattern[4]:
                    do += 1
                else:
                    do += 0
            if do >= 1:
                try:
                    user.follow()
                    print "Following"+str(i)
                    time.sleep(60)
                except:
                    count += 1
                    print count
                    time.sleep(60)
            else:
                count += 1
                print "skip"+str(count)
                time.sleep(60)
                
        

if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("")
