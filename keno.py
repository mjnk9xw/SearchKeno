from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument('-headless')
options.add_argument('-no-sandbox')
options.add_argument('-disable-dev-shm-usage')

# Options chrome
driver_chrome = webdriver.Chrome('chromedriver',options=options)
# End Options chrome

# Options firefox
# firefox_options = webdriver.FirefoxOptions()
# firefox_options.add_argument("--private")
# driver_firefox = webdriver.Firefox(firefox_options=firefox_options, executable_path='geckodriver')
# End Options firefox

m = {}
url = "https://www.minhchinh.com/xo-so-dien-toan-keno.html"
driver_chrome.get(url)
time.sleep(5)
for i in range(1):
    print('Loading page  : ',i+1)
    path_click = './/a[@href="javascript:chosePage('+str(i + 1)+')"]'
    print(path_click)
    try:
        click_button = driver_chrome.find_element_by_xpath(path_click)
        click_button.click()
    finally:
        elements = driver_chrome.find_elements_by_css_selector(".wrapperKQKeno")
        list_data = [str(el.text).replace('\n', ' ') for el in elements]
        for v in list_data:
            for v2 in v.split():
                if (v2.isdigit()):
                    m[v2] = m.get(v2, 0) + 1


print("len = ", len(m))
r_number = round(sum(m.values()) / len(m))
print("trung binh = ",r_number)
print(dict(sorted(m.items(), key=lambda item: item[1])))
print("danh sach so goi y = " , )
for k,v in m.items():
    if v == r_number-1:
        print(k)
