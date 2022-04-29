import tweepy
from twitter import Twitter, OAuth

# 認証に必要なキーとトークン
# API_KEY = ''
# API_SECRET = ''
# ACCESS_TOKEN = ''
# ACCESS_TOKEN_SECRET = ''
# BEARER_TOKEN=''
# Client_Secret = ''
client = tweepy.Client(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#つぶやくだけならbearer_tokenを指定しなくてもよい
client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
client.create_tweet(text='pythonから書き込んでます')
