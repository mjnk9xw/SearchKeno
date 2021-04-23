from selenium import webdriver
import requests
import time
options = webdriver.ChromeOptions()
options.add_argument('-headless')
options.add_argument('-no-sandbox')
options.add_argument('-disable-dev-shm-usage')

# Options chrome
driver_chrome = webdriver.Chrome('chromedriver',options=options)
# End Options chrome

url = "https://www.minhchinh.com/xo-so-dien-toan-keno.html"

def telegram_bot_sendtext(bot_message):
    
    bot_token = '1748992722:AAEhV689AR6nL-kqLxvuH1mWlp6jB_9uxJQ'
    bot_chatID = '-507701213'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

list_pre = {"1":0}
isFirst = True
from datetime import datetime
while True:
    
    now = datetime.now().time()
    if now.hour < 7 or now.hour > 22:
        time.sleep(3600)
        continue

    if isFirst == False:
        if now.minute % 10 != 1:
            time.sleep(30)
            continue

    isFirst = False
    driver_chrome.get(url)
    m = {}

    time.sleep(5)
    total = 0
    sotrung_kitruoc = ''
    for i in range(1):
        path_click = './/a[@href="javascript:chosePage('+str(i + 1)+')"]'
        try:
            click_button = driver_chrome.find_element_by_xpath(path_click)
            click_button.click()
        finally:
            elements = driver_chrome.find_elements_by_css_selector(".wrapperKQKeno")
            list_data = [str(el.text).replace('\n', ' ') for el in elements]
            checkPre = False
            for v in list_data:
                if checkPre == False:
                    sotrung_kitruoc = v
                for v2 in v.split():
                    if (v2.isdigit()):
                        if checkPre == False:
                            if v2 in list_pre.keys():
                                total += 1
                        m[v2] = m.get(v2, 0) + 1
                checkPre = True


    print("so du doan trung = ", total)
    print("xac suat du doan ki truoc = ", total/len(list_pre))
    r_number = round(sum(m.values()) / len(m))

    lst = []
    for k,v in m.items():
        if v == r_number-1:
            lst.append(int(k))

    if len(lst) < 6:
        for k,v in m.items():
            if len(lst) == 10:
                break
            if v == r_number:
                lst.append(int(k))

    lst.sort()
    print("danh sach so goi y = " , lst)
    telegram_bot_sendtext("danh sách số trúng kỳ trước = "+sotrung_kitruoc.replace('#', '') + f"số dự đoán trúng kì trước = {total} \n" + f"xác suất dự đoán kì trước = {total/len(list_pre)} \n" + f"danh sách gợi ý kì tới = {lst}")
    
    list_pre = {}
    for k in lst:
        list_pre[k]=1
    print("----------------------------------------------------------------------------------------------------------------------")
    # time.sleep(10*60)