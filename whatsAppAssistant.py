
import requests as res
import bs4
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from teastApi import getType 
import time
# import requests



def function():
    contact = input('Enter Name of victim : ')
    msg = input('Enter message : ')

    options=webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
    options.add_argument('--profile-directory=Default')
    # driver = webdriver.Chrome('D:\downloads\chromedriver',options=options)
    driver = webdriver.Chrome('D:\documents\internship_webscrapping\chromedriver',options=options)

    driver.get('https://web.whatsapp.com/')
    time.sleep(30)
    button=driver.find_element_by_xpath("//div[@class='_3FRCZ copyable-text selectable-text']")
    button.send_keys(contact)
    time.sleep(5)
    button.send_keys(Keys.ENTER)
    time.sleep(5)
    count=0
    prv=[]
    messageBar=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    while True:
        try :
            newMsg=driver.find_elements_by_xpath("//*[@id='pane-side']/div[1]/div/div/div[18]/div/div/div[2]/div[2]/div[2]/span[1]/div")
            newMsg.send_keys(Keys.ENTER)

        except:
            pass
        try:
            
    
            while True:
                try:
                    reply = driver.find_elements_by_xpath('//*[@class="_2hqOq message-in focusable-list-item"]/div/div/div/div[1]/div/span')
                    text2=[i.text for i in reply]
                    if prv!=text2:
                        prv=list(text2)
                        print(text2)
                    
                        for i in text2:
                            type=getType(i)
                            print(type)
                            if type=="greeting":
                                
                       
                        # msg="yes para man"
                        # messageBar.send_keys(msg,Keys.ENTER)

                                print("=================%==============")

                    count=count+1
                except :
                    print(count)
                #    print("Do you want to countinue :")
                #     option = input()
                #     if option=="n":
                #         break
                #     else: 
                #         pass
                    break
        except:
            print("Do you want to countinue :")
            option = input()
            if option=="n":
                break
            else:
                pass

if __name__ == "__main__":
    function()