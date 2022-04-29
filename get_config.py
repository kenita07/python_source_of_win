import configparser
import os
import pandas
import tweepy

config = configparser.ConfigParser(interpolation=None)


_BOT = 'bot'
_API_KEY = 'api_Key'
_API_KEY_SELECT = 'api_key_select'
_BEARER_TOKEN = 'bearer_token'
_ACCESS_TOKEN = 'access_token'
_ACCESS_TOKEN_SELECT = 'access_token_select'
_CLIENT_SECRET = 'client_secret'
_OPEN_PATH = 'account.ini'
_AMAZON = 'amazon'
_SBI = 'sbi' 
_ID = 'id'
_PASS = 'pass'

_APP_PATH = os.getcwd()
if '\\' in _APP_PATH:
    _APP_PATH = _APP_PATH.replace('\\', '/')


class GetConfig():
    def __init__(self):
        self.current_path = _APP_PATH
        config.read(_APP_PATH + '/config' + '/' + _OPEN_PATH)
        self.api_Key = config[_BOT][_API_KEY]
        self.api_key_select = config[_BOT][_API_KEY_SELECT]
        self.bearer_token = config[_BOT][_BEARER_TOKEN]
        self.access_token = config[_BOT][_ACCESS_TOKEN]
        self.access_token_select = config[_BOT][_ACCESS_TOKEN_SELECT]
        self.client_secret = config[_BOT][_CLIENT_SECRET]
        self.amazon_id = config[_AMAZON][_ID]
        self.amazon_pass = config[_AMAZON][_PASS]
        self.sbi_id = config[_SBI][_ID]
        self.sbi_pass = config[_SBI][_PASS]
        self.client = tweepy.Client(
            self.bearer_token,
            self.api_Key, self.api_key_select,
            self.access_token, self.access_token_select
        )
        