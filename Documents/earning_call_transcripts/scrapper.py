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
import pyautogui
from pathvalidate import is_valid_filename
from collections import OrderedDict
string = "I love python! It is such an amazing language."
time.sleep(3) # 3 second gap to avoid unwanted actions

company_scripts=pd.read_excel("company.xlsx")
ticker=company_scripts["Ticker"]
firm_name=company_scripts["Firm name"]
hash_map=OrderedDict()
for firm_count in range(2,len(ticker)):
    try:
        if hash_map.get(ticker[firm_count]):
            continue
        else:
            hash_map[ticker[firm_count]]=firm_count
            with open("firms_done.pickle","wb") as file:
                pickle.dump(hash_map,file)
            chromeOptions = webdriver.ChromeOptions()
            prefs = {"download.default_directory" : 'C:\\Users\\sudha\\Documents\\Stanford Securities\\pdf\\page1'}
            chromeOptions.add_experimental_option("prefs",prefs)
            chromeOptions.add_argument("window-size=1200x600")
            driver = webdriver.Chrome(options=chromeOptions)


            url=f'https://decodeinvesting.com/earnings_calls'
            driver.get(url)
            search= driver.find_element("xpath",'/html/body/div/div/div/div/div/div/div[2]/div/div/div/form/div[1]/div/div/input')
            search.send_keys(f"{firm_name[firm_count]}")
            pyautogui.press("down")
            time.sleep(2)
            pyautogui.press("enter")
            search.send_keys(Keys.ENTER)
            df_list=[]
            data={}
            k=1
            for i in range(1,51):
                col1= driver.find_element("xpath",f'/html/body/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[{k}]/div[1]')
                col2=driver.find_element("xpath",f'/html/body/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[{k}]/div[3]')
                col3=driver.find_element("xpath",f'/html/body/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[{k}]/div[4]')
            
                col4=driver.find_element("xpath",f'/html/body/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[{k}]/div[2]/a').get_attribute("href")
                                                
                                                
                data={"Date":[col1.text],"Quarter":[col2.text],"Year":[col3.text]}
                driver.get(col4)
                time.sleep(3)
                col5=driver.find_element("xpath",'//div//h4[@class="card-title"]')
                col6=driver.find_element("xpath",'//div[@class="card"]')
                print(col6.text)
                # transcripts=[]
                # for j in col6:
                #     transcripts.append(j.text)
                # transcripts1=' '.join(transcripts)
                # print(transcripts1)
                data.update({"Ticker":[col5.text],"Earning Call Transcripts":[col6.text]})
                df=pd.DataFrame(data=data)
                df_list.append(df)
                merged=pd.concat(df_list)
                merged.to_csv(f"{ticker[firm_count]}-{firm_name[firm_count]}.csv")
                
                driver.back()
                time.sleep(3)
                if i%10==0:
                    button=driver.find_element("xpath",'/html/body/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div[2]/button[2]')
                    button.click()
                    time.sleep(3)
                    k=1
                    continue
                k+=1


                time.sleep(3)
    except:
        hash_map[ticker[firm_count]]="Firm does not exist"
        continue
        
        



