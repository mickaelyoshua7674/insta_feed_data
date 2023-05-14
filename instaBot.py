from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
import traceback
import sys

def print_error():
    """Print the error message and exit script."""
    traceback.print_exc()
    print("Closing...")
    sys.exit()

class InstaBot:
    def __init__(self, username: str, chromedriver_path: str) -> None:
        self.USERNAME = username
        self.CHROMEDRIVER_PATH = chromedriver_path
        # INITIALIZING CHROME DRIVER
        print("Initializing Chrome driver...")
        try:
            op = webdriver.ChromeOptions()
            op.add_argument("headless") # don't open a Chrome window
            driver = webdriver.Chrome(executable_path=self.CHROMEDRIVER_PATH, options=op)
            print("Chrome driver initialized.\n")
        except:
            print("Error initializing Chrome driver...\n")
            print_error()

        # GET NUMBER OF PUBLISHMENTS
        print("Getting number of publishments...")
        try:
            driver.get(f"https://www.instagram.com/{self.USERNAME}/")
            time.sleep(3)
            num_publishments = driver.find_elements(By.CSS_SELECTOR, "._ac2a")[0].text
            self.num_publishments = int(re.sub("(\.)|(,)", "", num_publishments)) # remove . or , from text and turning into a int
            driver.quit()
            print("Number of publishments loaded.\n")
        except:
            print("Error getting numbers...\n")
            print_error()
        print("\n---------------------------------Object initialized successfully---------------------------------\n")
