try:
	import json
except ImportError:
	import simplejson as json
from twitter import Twitter,OAuth
from requests_oauthlib import OAuth1
import csv
import pandas as pd
import requests

ACCESS_TOKEN='1001763355001081856-bIqkKr2Wlv9Wh09dTQlC5oywsZIyqo'
ACCESS_SECRET='98ftA7Ugf9i8SGiPxLg5qUkuL5aT0GMNh6DCc2xM58lky'
CONSUMER_KEY='sDCUDdWy9UVc3O9yXNj9yuNK6'
CONSUMER_SECRET='x6yApBCjqf82hbFO1nDa5K4sXNTqh0lPmO9iMWyVEzgOb5Rfjq'

auth=OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
requests.get(url,auth=auth)
entity_url="https://api.twitter.com/1.1/statuses/retweets/"
colnames=["Similarity","Number","Text","Id"]
label=input("Enter the claim number:")
label="claim"+str(label)
inputFile=label+"_sorted.csv"
df=pd.read_csv(inputFile,names=colnames,sep="|")
values=df['Id']
for val in values:
	link=entity_url+str(val)+".json"
	r=requests.get(link,auth=auth)
	#for tweet in r.json()
	response=r.json()
	print(response)
	print('\n')
