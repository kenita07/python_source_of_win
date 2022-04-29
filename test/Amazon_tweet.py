import tweepy
from twitter import Twitter, OAuth
import configparser
import os 
import time



# 認証に必要なキーとトークン
# API_KEY = ''
# API_SECRET = ''
# ACCESS_TOKEN = ''
# ACCESS_TOKEN_SECRET = ''
# BEARER_TOKEN=''
# Client_Secret = ''
get_key_list=[]

moji='▼【Amazon直販】入荷速報♪=\n'
root_path = os.getcwd()


f = open(root_path + '\\amazon.txt', 'r', encoding='UTF-8')
data = f.read()
f.close()

tmp_get_key_list = [i for i in data.split('\n')]
for i in tmp_get_key_list:
    if '[' in i and ']' and '@amazon' not in i:
        get_key_list.append(i)
print(get_key_list)

for i in get_key_list:
    print(i)