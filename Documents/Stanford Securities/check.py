from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import pickle
import pyautogui
import keyboard


url='https://securities.stanford.edu/filings.html'
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : 'C:\\Users\\sudha\\Documents\\Stanford Securities\\pdf\\page1'}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("window-size=1200x600")
driver = webdriver.Chrome(options=chromeOptions)
with open("credentials.txt","r") as file:
    credentials=file.readlines()
    username=credentials[0]
    password=credentials[1]
    print("credential details",username,password)
driver.get(url)
login=driver.find_element("xpath",'//a[@href="#myModalLogin"]')
login.click()
time.sleep(3)

email = driver.find_element("xpath",'//input[@id="login_email"]')
password_field = driver.find_element("xpath",'//input[@id="login_pass"]')
email.send_keys(username.strip())
password_field.send_keys(password.strip())
time.sleep(2)
submit_btn = driver.find_element("xpath",'//div[@class="modal-footer"]//button[@type="submit"]')
print("Element is visible? " + str(submit_btn.is_displayed()))


password_field.send_keys(Keys.ENTER)
print("Logging In")
time.sleep(5)
driver.get("https://securities.stanford.edu/filings-documents/1082/OTI00108246/2023113_f01c_23CV21862.pdf")
pyautogui.hotkey('ctrl','s')
pyautogui.FAILSAFE=False
for i in range(10):
    pyautogui.press('enter')


time.sleep(10)