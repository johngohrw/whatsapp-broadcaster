from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from random import randint
from tkgui import runGUI
import tkinter as tk
import time
import datetime

returnValues = runGUI()

print(returnValues)

quit()

clearConsole = lambda: print('\n' * 150)

clearConsole()
print("Loading Chrome webdriver..")

browser = webdriver.Chrome()
browser.set_page_load_timeout(30)
delay = 5

clearConsole()
print("Loading WhatsApp Web..")

browser.get("https://web.whatsapp.com/")

try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Scan me!"]')))
    time.sleep(1)
except TimeoutError:
    print("Loading took too much time!")
    quit()

print("Please scan the QR code on the WhatsApp Web screen.")

try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//div[@id="pane-side"]')))
    time.sleep(1)
except TimeoutError:
    print("Loading took too much time!")
    quit()

# text = " Staling next to this, so the meme will be super-duper funny!! Get it? Get it? Cause communism, you know, its about making everything shared, right? So you see, this joke is so cle"
# browser.get("https://web.whatsapp.com/send?phone=60163232322&text=" + text + "&app_absent=0")