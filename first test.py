"""libraries"""
import io
import random
import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


logs_file = 'logs.log'
f = open(logs_file, "w")
f.write(f"start, {datetime.datetime.now()}\n")
f.close()
f = open(logs_file, "a")


def browser():
    try:
        chrome_options = webdriver.ChromeOptions()
        #chrome_options = Options()
        #chrome_options.add_argument("--headless")
        #chrome_options.setBinary("/home/andriy/PycharmProjects/mytower/chromedriver_linux64/chromedriver")
        chrome_options.add_argument("start-maximized")
        #chrome_options.add_argument("--blink-settings=imagesEnabled=false")
        chrome = webdriver.Chrome("/home/andriy/PycharmProjects/mytower/chromedriver_linux64/chromedriver")
        return chrome
    except Exception as e:
        print(e)


def open_site(chrome):
    try:
        chrome.switch_to.window(chrome.window_handles[0])
        chrome.get('https://panel.my-tower.co.il/')
        # chrome.get('https://dev-panel.my-tower.co.il/')
        chrome.implicitly_wait(10)
        f.write(f"successful opened site, {datetime.datetime.now()}\n")
        print('site is opened')
        chrome.execute_script("document.querySelector('#switch_left').click()")
        sleep(5)
        input_element = chrome.find_element_by_name("username")
        input_element.send_keys('demoadmin')
        input_element = chrome.find_element_by_name("password")
        input_element.send_keys('devaccountprod')
        sleep(5)
        chrome.execute_script("document.querySelector('.btn').click()")
        f.write(f"successful logged in, {datetime.datetime.now()}\n")
        print('logged in to the account')
        sleep(5)
    except Exception as e:
        f.write(f"Failed at opening and logging {e}, {datetime.datetime.now()}\n")
        print(e)


def sed_click(chrome):
    chrome.execute_script(
            "window.triggerMouseEvent = function triggerMouseEvent (node, eventType) { var clickEvent = document.createEvent ('MouseEvents'); clickEvent.initEvent (eventType, true, true); node.dispatchEvent (clickEvent); }")


def open_tasks(chrome):
    try:
        sleep(5)
        chrome.execute_script("document.querySelector('#menu > ul > li:nth-child(4) > span').click()")
        chrome.implicitly_wait(10)
        sleep(5)
        chrome.execute_script("document.querySelector('#menu > ul > li:nth-child(4) > ul > li:nth-child(8) > ul > li:nth-child(1) > a').click()")
        chrome.implicitly_wait(10)
        f.write(f"Tasks opened, {datetime.datetime.now()}\n")
        print("Tasks opened")
        sleep(10)
    except Exception as e:
        f.write(f"Failed at opening tasks {e},  {datetime.datetime.now()}\n")
        print(e)
        print(f"Failed at opening tasks")

def main():
    chrome = browser()
    open_site(chrome)
    sed_click(chrome)
    open_tasks(chrome)


if __name__ == '__main__':
    main()
