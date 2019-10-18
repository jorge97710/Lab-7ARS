
import csv
import pandas as pd
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth,wait_on_rate_limit=True) 
#####United Airlines 
# Open/Create a file to append data 
csvFile = open('trafico.csv', 'a') 
csvWriter = csv.writer(csvFile) 

for tweet in tweepy.Cursor(api.search,q="#TraficoGT",count=15000, since="2017-04-03", tweet_mode="extended").items(): 
    print (tweet.created_at, tweet.full_text, tweet.entities.keys()) 
    csvWriter.writerow(["Date", "Tweet", "Retweets", "user", "mentions"]) 
csvWriter.writerow([tweet.created_at, tweet.full_text.encode('utf-8'), tweet.retweet_count, tweet.user.name, tweet.entities['user_mentions']])
