from selenium import webdriver
from time import sleep
from datetime import datetime

uname = "CSMT"
passwd = "Csmt@234"
url = "https://172.22.4.73:8443/core/orionSplashScreen.do"
driver = webdriver.Chrome("E:\\chdrv\\chromedriverx.exe")

def conf():
    driver.get(url)
    driver.find_element_by_id("details-button").click()
    sleep(0.5)
    driver.find_element_by_id("proceed-link").click()
    sleep(0.5)
    driver.find_element_by_id("orion.dialog.box.ok").click()
    driver.find_element_by_id("name").send_keys(uname)
    driver.find_element_by_id("password").send_keys(passwd)
    driver.find_element_by_id("login.button").click()
    sleep(0.5)
    return driver
