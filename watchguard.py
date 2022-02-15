from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from openpyxl import workbook
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import os

driver = webdriver.Chrome('C:\\python\\chromedriver.exe')
driver.get("") # 장비 웹 도메인 입력
time.sleep(0.5)

#알수없는페이지 넘어가기
driver.find_element_by_xpath('//*[@id="details-button"]').click()
driver.find_element_by_xpath("//*[@id='proceed-link']").click()
driver.find_element_by_xpath("//*[@id='submit']").click()
time.sleep(0.3)

# 아이디와 비밀번호 입력
elem = driver.find_element_by_id("username").send_keys("") # 아이디 입력
time.sleep(0.3)
elem = driver.find_element_by_id ("password").send_keys("") # 패스워드 입력
time.sleep(0.5)
driver.find_element_by_xpath("/html/body/div/div/div[3]/form/button").send_keys(Keys.ENTER)
time.sleep(0.3)
# 메세지 읽고 넘어가기
check_mark = driver.find_element_by_xpath("//*[@id='read_accept']")
check_mark.click()
time.sleep(0.3)
driver.find_element_by_xpath("//*[@id='submit']").click()
# 방화벽접속 firewall 클릭
check_mark = driver.find_element_by_xpath("//*[@id='webui_nav_list']/li[4]/div").click()
time.sleep(0.5)
check_mark = driver.find_element_by_xpath("//*[@id='collapse3']/li[1]/a").click()

WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(
                (By.XPATH, r'//*[@id="grid_area"]/tbody'))
        )
time.sleep(1)

# test =   driver.find_element_by_xpath('//*[@id="gview_grid_area"]').get_attribute("outerHTML")
tables = driver.find_element_by_xpath('//*[@id="gview_grid_area"]/div[3]/div').get_attribute("outerHTML")
# print(tables)

table = BeautifulSoup(tables, 'html.parser')

# name=os.path.join( os.path.realpath(__file__),"test.txt")

# print(str(table))#수정함

f = open("./test.txt", 'w', encoding='utf8')
f.write(str(table))
f.close()

table_html = pd.read_html(str(table), flavor='lxml', header=0)[0].to_dict('records')
print(table_html)

def display_side_by_side(*args):
    """여러 데이터프레임 비교가 쉽게 옆쪽으로 표시한다"""
    f = open("./test.html", 'w',encoding='utf-8')
    html_str=''
    for df in args:
        html_str += df.to_html()
    f.write(html_str)
    f.close()
    # display_html(html_str.replace('table','table style="display:inline"'), raw=True)

df=pd.DataFrame(table_html)

df.to_excel('./test.xlsx')

# driver.quit()