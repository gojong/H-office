from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from openpyxl import workbook
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("") # nos 도메인 주소
time.sleep(0.5)


# 아이디와 비밀번호 입력
elem = driver.find_element_by_name("sid").send_keys("")# 아이디
time.sleep(0.3)
elem = driver.find_element_by_name("passwd").send_keys("") # 패스워드
time.sleep(0.5)
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[3]/td/input").send_keys(Keys.ENTER)
time.sleep(3)

#################### 1회 반복하는거
noc = driver.find_element_by_xpath('//*[@id="my_noc"]')
# print(len(noc.find_elements_by_tag_name('a')))
for i in range(len(noc.find_elements_by_tag_name('a'))):
            # try:
            time.sleep(.5)
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located(
                    (By.XPATH, r'//*[@id="my_noc"]'))
            )
            time.sleep(.5)
            driver.find_element_by_xpath('//*[@id="my_noc"]/a[1]').click()

            time.sleep(.5)
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located(
                    (By.XPATH, r'//*[@id="alarm_noc"]'))
            )
            time.sleep(.5)
            driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="alarm_noc"]'))
            try:
                WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located(
                        (By.XPATH, r'//*[@id="alarm_form"]/table[2]/tbody/tr[6]/td/span[3]/div[2]/div/textarea'))
                )
                driver.find_element_by_xpath('//*[@id="alarm_form"]/table[2]/tbody/tr[6]/td/span[3]/div[2]/div/textarea').send_keys("완료")
                driver.find_element_by_xpath('//*[@id="alarm_form"]/table[2]/tbody/tr[7]/td/input').click()
            
            except:
                WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located(
                        (By.XPATH, r'//*[@id="alarm_form"]/table[2]/tbody/tr[7]/td/span[2]/div[2]/div/textarea'))
                )
                driver.find_element_by_xpath('//*[@id="alarm_form"]/table[2]/tbody/tr[7]/td/span[2]/div[2]/div/textarea').send_keys("완료")
                driver.find_element_by_xpath('//*[@id="alarm_form"]/table[2]/tbody/tr[8]/td/input[2]').click()
            
            try:
                WebDriverWait(driver, 3).until(EC.alert_is_present())
                alert = driver.switch_to.alert
                
                # 취소하기(닫기)
                alert.dismiss()
                
                # 확인하기
                alert.accept()
            except:
                print("no alert")

            driver.switch_to.window(driver.current_window_handle)

            print(str(i+1)+'번쨰 완료')

    # except :
        # WebDriverWait(driver, 3).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, r'//*[@id="my_noc"]/a['+str(i+1)+']/span'))
        # )
        # driver.find_element_by_xpath('//*[@id="my_noc"]/a['+str(i+1)+']/span').click()
