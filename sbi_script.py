
from ast import Return
import time                                 # スリープを使うために必要
from selenium import webdriver              # Webブラウザを自動操作する（python -m pip install selenium)
import chromedriver_binary                  # パスを通すためのコード
from get_config import GetConfig
import json
import time


_URL = 'url'
_URL_VALUE = 'sbi_login_home'
_MEIGARA = 'https://site2.sbisec.co.jp/ETGate/?stock_sec_code_mul=XXXX&exchange_code=TKY&i_stock_sec=XXXX&i_exchange_code=TKY&i_output_type=0&i_dom_flg=1&_ControlID=WPLETsiR001Control&_PageID=WPLETsiR001Ilst10&_ActionID=getDetailOfStockPriceJP&getFlg=on'

_OUTPUT = '/output/kabuka_pbr.json'
_OUTPUT_PARSE = '/output/kabuka_pbr_parse.json'
# class SeleniumDriver():
#     # 非表示実行ソース
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')
#     driver = webdriver.Chrome(options=options)  # 今は chrome_options= ではなく options=
#     driver.get('https://www.google.com/')
#     print(driver.title)

#     search_box = driver.find_element_by_name("q")
#     search_box.send_keys('ChromeDriver')
#     search_box.submit()
#     print(driver.title)

#     driver.save_screenshot('search_results.png')
#     driver.quit()
    
    
class SBI_process():
    def __init__(self, login_home):
        # SBIログイン
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)    # Chromeを準備
        # self.driver = webdriver.Chrome()                 # Chromeを準備
        
        self.driver.get(login_home)                           # URLを開く
        self.id = self.driver.find_element_by_name('user_id')   # HTML内でテキストボックス(name='email')を指定する
        self.id.send_keys(conf.sbi_id)                # テキストボックスを送信する
        self.pw = self.driver.find_element_by_name('user_password')  # HTML内でテキストボックス(name='password')を指定する
        self.pw.send_keys(conf.sbi_pass)              # テキストボックスを送信する
        self.login = self.driver.find_element_by_name('ACT_login')
        self.login.click()                                 # クリック
        
        
        # 検索実行
        for i in range(1300,9999):
            tar_url = _MEIGARA.replace('XXXX', str(i))
            self.driver.get(tar_url)
            self.kabuka = self.driver.find_element_by_name('FormKabuka')
            if self.kabuka.text != '対象銘柄はありません。または、表示できません。':
                tar_meigara = self.kabuka.text.split('\n')[0]
                tar_pbr = self.kabuka.text.split('実績PBR')[1].split('\n')[1].replace('倍','')
                tar_kabuka = self.kabuka.text.split('出来高')[1].split('\n')[1].replace('倍','')
                if tar_pbr == '--':
                    continue
                tar_dict.setdefault(tar_meigara + '/' + tar_kabuka, tar_pbr)
                print(tar_meigara)
            else:
                pass
            time.sleep(10)
        
def dict_process(path):
    with open(path, 'w', encoding ='utf-8') as f:
        json.dump(tar_dict, f, indent = 4, ensure_ascii = False)

    
if __name__ == '__main__':
    conf = GetConfig()
    json_open = open(conf.current_path + '/config/url.json', 'r')
    json_load = json.load(json_open)
    login_home = json_load[_URL][_URL_VALUE]
    tar_dict = {}
    sbi_class = SBI_process(login_home)
    dict_process(conf.current_path + _OUTPUT)

    for k, v in list(tar_dict.items()):
        # PBR閾値
        if float(v) >= 2:
            tar_dict.pop(k)
    dict_process(conf.current_path + _OUTPUT_PARSE)
