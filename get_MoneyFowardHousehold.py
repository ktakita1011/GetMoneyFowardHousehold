import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

def get_df_from_table_elements(trs):
    lines = []
    for i in range(1,len(trs)):
        tds = trs[i].find_elements(By.TAG_NAME, "td")
        line = []
        for j in range(0,len(tds)):
            if j < len(tds)-1:
                line.append("%s\t" % (tds[j].text))
            else:
                line.append("%s" % (tds[j].text))
        lines.append(line)

    df = pd.DataFrame(lines)
    df.columns = ['品目', '金額', '割合']
    df['割合'] = df['割合'].str.replace('%', '').astype(float)
    df['品目'] = df['品目'].str.replace('\t', '')
    df['金額'] = df['金額'].str.replace('円\t', '')
    df['金額'] = df['金額'].str.replace(',', '').astype(int)
    return df

browser = webdriver.Chrome(r'C:\slenium\chromedriver.exe')

url = 'https://id.moneyforward.com/sign_in/email'
browser.get(url)
sleep(3)
EMAIL = os.environ['MONEYFOWARD']
PASS = os.environ['MONEYFOWARD_PASS']
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

#予算ページに動く
goto_kakei = browser.find_element_by_xpath(
    '//*[@id="header-container"]/header/div[2]/ul/li[2]/a'
)
goto_kakei.click()
sleep(3)

goto_shushi = browser.find_element_by_xpath(
    '//*[@id="functions-menu-container"]/ul/li[2]/a'
)
goto_shushi.click()
sleep(3)

table = browser.find_element_by_id('table-outgo')
trs = table.find_elements(By.TAG_NAME, "tr")

df = get_df_from_table_elements(trs)
df.to_csv('収支一覧.csv')