import tweepy
from datetime import datetime as dt

# 認証に必要なキーとトークン
# API_KEY = ''
# API_SECRET = ''
# ACCESS_TOKEN = ''
# ACCESS_TOKEN_SECRET = ''
# BEARER_TOKEN=''
# Client_Secret = ''


dt_now = dt.now()
yyyy = str(dt_now.year) + '年'
mm = str(dt_now.month) + '月'
dd = str(dt_now.day) + '日'
kintore = 'リストカール10回*2セット行いました。'
client = tweepy.Client(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#つぶやくだけならbearer_tokenを指定しなくてもよい
client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

tweet_content = yyyy + mm + dd + kintore
client.create_tweet(text = tweet_content)
