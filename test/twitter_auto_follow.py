import tweepy
from twitter import Twitter, OAuth
import time                                 # スリープを使うために必要
from get_config import GetConfig

user_id = 'amaamasuke'

if __name__ == '__main__':
    conf = GetConfig()
    conf.client.follow_user(target_user_id=user_id)
    # conf.client.create_tweet(text='tesuto')
    # conf.client.block(target_user_id = user_id)