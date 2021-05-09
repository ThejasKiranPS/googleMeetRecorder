from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pause
import pynput
import os
from pynput.keyboard import Key, Controller
from datetime import datetime
#######YEAR#MONTH#DAY#HOUR#MINUTE###### DO NOT PUT ZERO BEFORE A NUMBER
# pause.until(datetime(2020, 3, 27, 11, 29))
# MAIL & PASSWORD (THE MAIL U WILL USE TO ENTER TO THE MEET)


def check_participants(participants_list):
  print(f"{participants_list}")
  with open("list.csv", 'r', encoding = 'utf-8') as f:
    list=f.readlines()
    for count in range(len(list)):
      list[count]=list[count].replace('\n', '')
      for item in participants_list:
        if list[count] in item:
          print("Teacher Present")
          import recording
          teacher_present = True



usernameStr = 'Enter Your Mail Address Here'
passwordStr = 'Enter Your Password'
url_meet = 'nsm-xovs-nuf'
options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,     # 1:allow, 2:block
    "profile.default_content_setting_values.media_stream_camera": 2,
     "profile.default_content_setting_values.notifications": 2
  })
browser = webdriver.Chrome(chrome_options=options)
browser.maximize_window()
browser.get(f"https://accounts.google.com/AccountChooser/identifier?continue=https%3A%2F%2Fmeet.google.com%2F{url_meet}&hl=en&flowName=GlifWebSignIn&flowEntry=AccountChooser")
username = browser.find_element_by_id('identifierId')
username.send_keys(usernameStr)
nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()
time.sleep(5)
keyboard = Controller()
#keyboard.type(passwordStr)
password = browser.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
password.send_keys(passwordStr)
#keyboard.type(passwordStr)
signInButton = browser.find_element_by_id('passwordNext')
signInButton.click()
time.sleep(6)
#element = browser.find_element_by_class_name('CwaK9')
#browser.execute_script("arguments[0].click();", element)
browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span').click()
time.sleep(6)
flag = True
element_listb = browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[1]/div[3]/div/div[2]/div[1]/span/span')
element_listb.click()

while flag:

  element_list = browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[1]/div[1]/div[2]/div')
  check_participants(element_list.text.split('\n'))
  time.sleep(60)
