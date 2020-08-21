import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

INIT_LOGIN_XPath = '/html/body/div/div/div/div/main/div/div/div/div[1]/div/a[2]/div/span/span'
LOGIN_XPath = '/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div/span/span'
EMAIL_XPath ='/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input'
PASSWORD_XPath = '/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input'
TWEETBOX_XPath = '''/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[
                    2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/
                    div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'''
TWEETBUTTON_XPath ='''/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]
                        /div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span'''

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
op.add_argument('--headless')
op.add_argument('--no-sandbox')
op.add_argument('--disable-dev-sh-usage')

# driver = webdriver.Chrome('drivers\chromedriver.exe')
driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'),chrome_options=op)

driver.get('https://twitter.com/')
print('-Loaded Twitter')
driver.find_element_by_xpath(INIT_LOGIN_XPath).click()
try:
    element =   WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,EMAIL_XPath))
    )
    element.send_keys(os.environ.get('EMAIL'))
    element =   WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,PASSWORD_XPath))
    )
    element.send_keys(os.environ.get('PASSWORD'))
    element =   WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,LOGIN_XPath))
    )
    element.click()
    element =   WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,TWEETBOX_XPath))
    )
    print('-Logged in')
    element.send_keys(os.environ.get('TWEET_STRING'))
    element =   WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,TWEETBUTTON_XPath))
    )
    element.click()
except:
    print('-Problem tweeting.')
finally:
    driver.quit()
