#You need to download chromedriver compatible with your current browser build
#https://sites.google.com/a/chromium.org/chromedriver/downloads

from logging import info
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')

PATH = f"\chromedriver.exe" # <----Path to chromedriver.exe
driver = webdriver.Chrome(PATH, chrome_options=options)

driver.get("https://water.srpnet.com/quick-view/schedule")
time.sleep(3)

try:
    search = driver.find_element_by_id("mat-input-0")
    print("Looking up account...")
    
except:
    print("search bar not found")

search.send_keys("xxxxxxx") #<------Enter account# here
search.send_keys(Keys.RETURN)
print("Waiting for response...")

time.sleep(4)

try:
    info = driver.find_element_by_class_name("schedule-info")
    print("Current posted start time is:")
    print(info.text)
except:
    print("cold not get times")

driver.quit()