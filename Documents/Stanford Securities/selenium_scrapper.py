#finona6177@eazenity.com
#Password@1234
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import pickle
import pyautogui
import keyboard as kbd # importing keyboard module
import time
string = "I love python! It is such an amazing language."
time.sleep(3) # 3 second gap to avoid unwanted actions

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

name=[]
filing_date=[]
headquarters=[]
ticker=[]
district=[]
exchange=[]

k=0
for i in td:
    print(i.text)
    if k==0:
        name.append(i.text)
    elif k==1:
        filing_date.append(i.text)
    elif k==2:
        district.append(i.text)
    elif k==3:
        exchange.append(i.text)
    elif k==4:
        ticker.append(i.text)
        k=0
        continue
        
    k+=1
print("Companies",name)
name.insert(0,0)
print(len(name))
df_list=[]
headquar=[]
pub=[]
for i in range(1,len(name)):
   
    specific_td=driver.find_element("xpath",f'//table//tbody//tr[{i}]//td[1]')
    
    specific_td.click()
    public=driver.find_element("xpath",f'//div[@class="span4"][strong="Market Status:"]')
    print(public.text)
    headquarters=driver.find_element("xpath",f'//div[@class="span4"][strong="Headquarters:"]')
    headquar.append(headquarters.text)
    pub.append(public.text)
    
        
    td1=driver.find_elements("xpath",'//*[@id="fic"]/table/tbody/tr')
    print(len(td1))
    for j in range(len(td1)):
        current_url=driver.current_url
        public=driver.find_element("xpath",f'//*[@id="fic"]/table/tbody/tr[{j+1}]/td[2]')
        public.click()
        pyautogui.hotkey('ctrl','s')
        time.sleep(3)
        pyautogui.FAILSAFE=False
        
        kbd.write(name[i]+str(j+1),0.1)
        time.sleep(3)










        
        for k in range(10):
            pyautogui.press('enter')
        driver.get(current_url)
        
        
    driver.get(url)
    
name.pop(0)
print(len(name),len(filing_date),len(district),len(exchange),len(ticker),len(headquar),len(pub))
data={"Filing Name":name,"Filing Date":filing_date,"District Court":district,"Exchange":exchange,"Ticker":ticker,"HeadQuarters":headquar,"Listing":pub}
df=pd.DataFrame(data=data)
df.to_csv("filings.csv")    

    
    
#//*[@id="fic"]/table/tbody/tr[2]/td[2]