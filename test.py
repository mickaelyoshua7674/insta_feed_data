from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHROMEDRIVER_PATH = "chromedriver.exe"

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
driver.get("chrome://settings/clearBrowserData")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.ENTER)
time.sleep(100)