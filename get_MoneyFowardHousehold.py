from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

browser = webdriver.Chrome('C:\\selenium\\chromedriver.exe')

url = 'https://id.moneyforward.com/sign_in/email'
browser.get(url)
sleep(3)
EMAIL = 'email'
PASS = 'pass'
# Enter email
elem_loginMethod = browser.find_element_by_xpath(
    '/html/body/main/div/div/div/div/div[1]/section/form/div[2]/div/input')
elem_loginMethod.send_keys(EMAIL)

# Jump to password input page
elem_login = browser.find_element_by_xpath(
    '/html/body/main/div/div/div/div/div[1]/section/form/div[2]/div/div[3]/input')
elem_login.click()
sleep(3)

# Enter password
elem_password = browser.find_element_by_xpath(
    '/html/body/main/div/div/div/div/div[1]/section/form/div[2]/div/input[2]')
elem_password.send_keys(PASS)
elem_password.click()
sleep(3)

elem_login = browser.find_element_by_xpath(
        '/html/body/main/div/div/div/div/div[1]/section/form/div[2]/div/div[3]/input')
elem_login.click()
sleep(3)

goto_ME = browser.find_element_by_xpath(
        '/html/body/main/div/div/div/div[1]/div/ul/li[1]/a/img')
goto_ME.click()
sleep(3)
goto_ME = browser.find_element_by_xpath(
        '/html/body/main/div/div/div/div/div[1]/section/form/div[2]/div/div[2]/input')
goto_ME.click()
sleep(3)
goto_yosan = browser.find_element_by_xpath(
    '//*[@id="header-container"]/header/div[2]/ul/li[3]/a'
)
goto_yosan.click()
sleep(3)


