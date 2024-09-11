from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://comic.naver.com/webtoon")
time.sleep(2)

menuList = driver.find_elements(by=By.CSS_SELECTOR, value='.SubNavigationBar__snb_wrap--A5gfM > nav > ul > li > a')

menuNameList = []

for menu in menuList[1:8]: # 슬라이싱
    menu.click()
    menuNameList.append(menu.text)
    time.sleep(1)

    webtoonList = driver.find_elements(by=By.CSS_SELECTOR, value='.ContentList__content_list--q5KXY > .item')
    for webtoon in webtoonList:
        driver.execute_script("arguments[0].scrollIntoView(true);", webtoon)
        time.sleep(0.2)
        posterImg = webtoon.find_element(by=By.CSS_SELECTOR, value='img') 
        posterImgUrl = posterImg.get_attribute(name="src")
        print(posterImgUrl)

print(f"메뉴이름리스트: {menuNameList}") # 문자열 앞에 f

 
