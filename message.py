
import requests as res
import bs4
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


def function():
    contact = input('Enter Name of victim : ')
    msg = input('Enter message : ')

    options=webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
    options.add_argument('--profile-directory=Default')


    driver = webdriver.Chrome('D:\downloads\chromedriver',options=options)
    driver.get('https://web.whatsapp.com/')
    # driver.get('https://www.google.com')
    # button = driver.find_element_by_class_name('_3FRCZ copyable-text selectable-text')
    time.sleep(30)
    button=driver.find_element_by_xpath("//div[@class='_3FRCZ copyable-text selectable-text']")
    button.send_keys(contact)
    time.sleep(5)
    button.send_keys(Keys.ENTER)
    time.sleep(5)
    count=0
    # while True:
        # messageBar = driver.find_element_by_xpath("//div[@class='_3uMse']")
        # messageBar.send_keys(msg,Keys.ENTER)
    while True:
        # messageBar = driver.find_element_by_xpath("//div[@class='_3uMse']")
        # messageBar=driver.find_elements_by_class_name('_3uMse')



        # try:
        #     messageBar=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        #     messageBar.send_keys(msg,Keys.ENTER)
        #     count=count+1
        # except :
        #     print(count)
        #     break
        try:
            # reply = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]/div[23]/div/div/div/div[1]/div/span[1]/span')
           
            # reply=driver.find_elements_by_name('')
            # val='[4:19 pm, 16/08/2020] Amma: '
            # reply2 = driver.find_element_by_xpath('//div[@data-pre-plain-text="[4:19 pm, 16/08/2020] Amma: "]')
            # text2=[i.text for i in reply2]
            # print(text2)
            # print("=================%==============")

            # message = driver.find_elements_by_class_name("vW7d1")
            # print(message.text)
            # print(reply.text)
            # try :
            #     message = driver.find_elements_by_class_name("vW7d1")[-1]
            # except:
            #     pass
            # print("hello")
          
            # print(text)
            # print(text)
            # for t in text:
            #     wrd=''
            #     flag=0
            #     if "pickachu" in t:
            #         # pass
            #         # print("hello")
            #         while True:
            #             try:
            #                 messageBar=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            #                 messageBar.send_keys(msg,Keys.ENTER)
            #                 count=count+1
            #             except :
            #                 print(count)
            #                 break
            # print("here")
            # emojDrawer = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div/button[2]/span')
            # print('heree')
            # celebEmoj = driver.find_element_by_xpath('//*[@id="main"]/footer/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div[10]/div/div/div/span[2]')

            while True:
                try:
                    # reply=driver.find_elements_by_class_name('_274yw')
                    # replyTmp=driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]/div[21]')
                    # 
                    # textTmp=[j.text for j in replyTmp]
                    # text = [i.text for i in reply]
                    # print(text)
                    

                    messageBar=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                    messageBar.send_keys(msg,Keys.ENTER)


                    # messageBar.send_keys(msg,)
                    # emojDrawer.click()
                    # celebEmoj.click()
                    # celebEmoj.click()
                    # celebEmoj.click()
                    count=count+1
                except :
                    print(count)
                    break
                        # reply2=driver.find_elements_by_class_name('_274yw')
                        # text2 = [i.text for i in reply2]
                        # for kj in text2:
                        #     if stop in kj:
                        #         flag=1
                        #         break


        except:
            print("no reply yet :")
            print("do you wish to send msg:")
            break
        print("=================")

    # time.sleep(100)


if __name__ == "__main__":
    function()