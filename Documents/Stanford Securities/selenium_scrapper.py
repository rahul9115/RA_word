from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import pickle
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

td=driver.find_elements("xpath",'//td')
df=pd.DataFrame()
l=[]
k=0
for i in td:
    print(i.text)
    if k%5==0:
        l.append(i.text)
    k+=1
print(l[0])
l.insert(0,0)
print(len(l))
driver.close()
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : f'C:\\Users\\sudha\\Documents\\Stanford Securities\\pdf\\{l[1]}'}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("window-size=1200x600")
driver = webdriver.Chrome(options=chromeOptions)
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
for i in range(1,len(l)):
   
    specific_td=driver.find_element("xpath",f'//table//tbody//tr[{i}]//td[1]')
    
    specific_td.click()
    public=driver.find_element("xpath",f'//div[@class="span4"][strong="Market Status:"]')
    print(public.text)
    if "Public (Listed)" in public.text:
        print(True)
    
    
    
        
    td1=driver.find_elements("xpath",'//*[@id="fic"]/table/tbody/tr')
    print(len(td1))
    for j in range(len(td1)):
        current_url=driver.current_url
        public=driver.find_element("xpath",f'//*[@id="fic"]/table/tbody/tr[{j+1}]/td[2]')
        public.click()
        driver.get(driver.current_url)
        driver.get(current_url)
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : f'C:\\Users\\sudha\\Documents\\Stanford Securities\\pdf\\{l[i+1]}'}
    chromeOptions.add_experimental_option("prefs",prefs)
    chromeOptions.add_argument("window-size=1200x600")
    driver = webdriver.Chrome(options=chromeOptions)
    driver.get(url)
    break

    
    

# //*[@id="records"]/table/tbody/tr[9]/td[1]  
# //*[@id="fic"]/table/tbody/tr[1]/td[2]
# //*[@id="fic"]/table/tbody/tr[2]/td[2]
# //*[@id="fic"]/table/tbody/tr[1]/td[2]
# //*[@id="fic"]/table/tbody/tr[2]/td[2]
# //*[@id="fic"]/table/tbody/tr[1]/td[2]
# //*[@id="records"]/table/tbody/tr[30]/td[1]
# //*[@id="fic"]/table/tbody/tr[1]
# //*[@id="fic"]/table/tbody/tr[1]

# //*[@id="fic"]/table/tbody/tr[1]