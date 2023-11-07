from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import pickle
url='https://securities.stanford.edu/filings.html'
chromeOptions = webdriver.ChromeOptions()
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

td=driver.find_elements("xpath",'//td')
df=pd.DataFrame()
l=[]
k=0
for i in td:
    print(i.text)
    if k%5==0:
        l.append(i.text)
    k+=1
print(l)

