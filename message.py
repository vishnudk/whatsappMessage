
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
    driver = webdriver.Chrome('D:\downloads\chromedriver')
    driver.get('https://web.whatsapp.com/')
    # driver.get('https://www.google.com')
    # button = driver.find_element_by_class_name('_3FRCZ copyable-text selectable-text')
    time.sleep(20)
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
        messageBar=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        messageBar.send_keys(msg,Keys.ENTER)
        count=count+1
    print(count)
    time.sleep(100)


if __name__ == "__main__":
    function()