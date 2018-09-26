# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 14:54:40 2018

@author: Rishav
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import argparse
import time
import os


def SEARCHER(search):
    output=os.getcwd()+os.sep+"URLS"
    print(output)
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory' : output}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://google.co.in/")
    wait=WebDriverWait(driver,500)
    
    # Search Google Using The Given Topic
    search_arg="//*[@id='lst-ib']"
    Input= wait.until(EC.presence_of_element_located((By.XPATH, search_arg)))    
    Input.send_keys(search+Keys.ENTER)
    
    #Click on the Image TAB
    image_arg="//*[@id='hdtb-msb-vis']/div[2]/a"
    Input= wait.until(EC.presence_of_element_located((By.XPATH, image_arg)))
    Input.click()
    
    #Move to the end of the page and find the Find More Results Button
    elm=driver.find_element_by_tag_name('html')
    print("[INFO] Searching {}.".format(search))
    while(1):
        try:
            elm.send_keys(Keys.END)
            elm2=driver.find_element_by_xpath("//*[@id='smb']")
            elm2.send_keys(Keys.ENTER)
            time.sleep(5)
            break
        except:
            print(".",end="")
            
    
    while(1):
        try:
            elm.send_keys(Keys.END)
            elm2=driver.find_element_by_xpath("//*[@id='cnt']/div[4]")
            print("[INFO] Done Searching")
            break
        except KeyboardInterrupt:
            break
        except:
            print(".",end="")
    
    print("[INFO] Searching Completed")

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("-s","--search",required=True,help="Searches the images on the Google Images")
    args=vars(ap.parse_args())
    SEARCHER(args["search"])
