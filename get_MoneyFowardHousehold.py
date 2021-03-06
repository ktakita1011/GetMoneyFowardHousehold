import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import pandas as pd

class CFG:
    sleep_sec = 1

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

def get_xpath_text(xpath):
    element = browser.find_element_by_xpath(xpath)
    return element.text

def click_before_month_summary():
    before_summary_xpath = '//*[@id="b_range"]'
    click_this = browser.find_element_by_xpath(
    before_summary_xpath)
    click_this.click()

browser = webdriver.Chrome(r'C:\slenium\chromedriver.exe')

url = 'https://id.moneyforward.com/sign_in/email'
browser.get(url)
sleep(CFG.sleep_sec)

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
sleep(CFG.sleep_sec)

# Enter password
elem_password = browser.find_element_by_xpath(
    '/html/body/main/div/div/div/div/div[1]/section/form/div[2]/div/input[2]')
elem_password.send_keys(PASS)
elem_password.click()
sleep(CFG.sleep_sec)

elem_login = browser.find_element_by_xpath(
        '/html/body/main/div/div/div/div/div[1]/section/form/div[2]/div/div[3]/input')
elem_login.click()
sleep(CFG.sleep_sec)

goto_ME = browser.find_element_by_xpath(
        '/html/body/main/div/div/div/div[1]/div/ul/li[1]/a/img')
goto_ME.click()
sleep(CFG.sleep_sec)
goto_ME = browser.find_element_by_xpath(
        '/html/body/main/div/div/div/div/div[1]/section/form/div[2]/div/div[2]/input')
goto_ME.click()
sleep(CFG.sleep_sec)

#予算ページに動く
goto_kakei = browser.find_element_by_xpath(
    '//*[@id="header-container"]/header/div[2]/ul/li[2]/a'
)
goto_kakei.click()
sleep(CFG.sleep_sec)

goto_shushi = browser.find_element_by_xpath(
    '//*[@id="functions-menu-container"]/ul/li[2]/a'
)
goto_shushi.click()
sleep(CFG.sleep_sec)

#毎回使うXpath
summary_range_xpath = '//*[@id="select-month"]/table/tbody/tr/td[2]/div[1]'

#今の最新月の収支get
table = browser.find_element_by_id('table-outgo')
trs = table.find_elements(By.TAG_NAME, "tr")
df = get_df_from_table_elements(trs)

yyyymm = get_xpath_text(summary_range_xpath)[:7]
output_df = df.rename(columns={'金額': f'{yyyymm}_金額', '割合': f'{yyyymm}_割合'})
output_df = output_df.set_index('品目')

for i in range(1,12):
    click_before_month_summary()
    sleep(CFG.sleep_sec)
    table = browser.find_element_by_id('table-outgo')
    trs = table.find_elements(By.TAG_NAME, "tr")
    yyyymm = get_xpath_text(summary_range_xpath)[:7]
    df = get_df_from_table_elements(trs)
    df = df.rename(columns={'金額': f'{yyyymm}_金額', '割合': f'{yyyymm}_割合'})
    df = df.set_index('品目')
    output_df = pd.concat([output_df, df], axis=1)

output_df.to_csv('収支一覧.csv')