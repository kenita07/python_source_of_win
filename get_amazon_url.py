
import time                                 # スリープを使うために必要
from selenium import webdriver              # Webブラウザを自動操作する（python -m pip install selenium)
import chromedriver_binary                  # パスを通すためのコード
from get_config import GetConfig

_HOME = 'https://www.amazon.co.jp/gp/buyagain/ref=pd_gwd_bag_pd_gw_rp?ie=UTF8&ats=eyJleHBsaWNpdENhbmRpZGF0ZXMiOiJCMDdORDVKNUZXLEIwOEcxUFdOOVgsQjAwNE4zQVBHTyxCMDdLM0RWVDlCIiwiY3VzdG9tZXJJZCI6IkEzNjdGSTFUTTJZNkZJIn0%3D&pd_rd_w=geuzV&pf_rd_p=1ec56066-77d2-4e8e-8e55-53dd762734bc&pf_rd_r=VXMYJBCC6S33PCSZQHNE&pd_rd_r=79d29228-1308-4c1b-b41f-f7076cfe6d30&pd_rd_wg=Ggt8l'

        
class AmazonLogin():
    def __init__(self):
        self.driver = webdriver.Chrome()                 # Chromeを準備
        self.driver.get(_HOME)                           # Googleを開く
        self.id = self.driver.find_element_by_name('email')   # HTML内でテキストボックス(name='email')を指定する
        self.id.send_keys(conf.amazon_id)                # テキストボックスを送信する
        self.id.submit()                                 # 実行
        self.pw = self.driver.find_element_by_name('password')  # HTML内でテキストボックス(name='password')を指定する
        self.pw.send_keys(conf.amazon_pass)              # テキストボックスを送信する
        self.pw.submit()                                 # 実行

class AmazonURLSearch():
    def __init__(self):
        self.aaa = 123
        
        
        
if __name__ == '__main__':
    conf = GetConfig()
    AmazonLogin()
    print(21)