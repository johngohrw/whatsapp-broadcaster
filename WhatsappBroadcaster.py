from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from random import randint
from tkgui import runGUI
from utils import RepresentsInt, clearConsole, isValidNumber, stripNonNumeric, printArt, printInline, printReplace
from colorama import init
from colorama import Fore, Back, Style
import tkinter as tk
import time
import datetime

init(autoreset=True) # init colorama
printArt()
print(Fore.YELLOW + "This program requires ChromeDriver to work.\n"+ Style.RESET_ALL +"You can download it here: {}https://chromedriver.chromium.org/downloads".format(Fore.CYAN))
print("Choose the right version of ChromeDriver according to your computer's Chrome version.\nYou can check your Google Chrome version by:\n\n  Chrome's top-right menu > Help > About Google Chrome\n")
print("Please make sure you have the right ChromeDriver file in the same directory as " + Fore.GREEN + "WhatsappBroadcaster.exe")

returnValues = runGUI()
phones = returnValues["phones"].split('\n')
message = returnValues["message"].replace("\n", "%0A")
interval = returnValues["interval"]

if (not RepresentsInt(interval)): 
    print("Interval value is not a number, please try again.")
    input("Press Enter key to Quit")
    quit()

clearConsole()
print("Loading Chrome webdriver..")

browser = webdriver.Chrome()
browser.set_page_load_timeout(30)
delay = 40
whatsappLoadDelay = 30
chatLoadDelay = 60

clearConsole()
print("Loading WhatsApp Web..")

browser.get("https://web.whatsapp.com/")

try:
    myElem = WebDriverWait(browser, whatsappLoadDelay).until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Scan me!"]')))
    time.sleep(1)
except TimeoutError:
    browser.close()
    print("Loading took too much time!")
    input("Press Enter to quit")
    quit()

print("Please scan the QR code on the WhatsApp Web screen.")

try:
    myElem = WebDriverWait(browser, 10000).until(EC.presence_of_element_located((By.XPATH, '//div[@id="pane-side"]')))
    time.sleep(1)
except TimeoutError:
    browser.close()
    print("Loading took too much time!")
    input("Press Enter to quit")
    quit()

print("Login success!")

time.sleep(1)
printInline("Starting broadcasting in 3..")
time.sleep(1)
printInline(" 2..")
time.sleep(1)
print(" 1..")
time.sleep(1)

success = 0
fail = 0
for number in phones:
    phone = stripNonNumeric(number)
    printInline("> (sending to " + phone + ")")
    if (not isValidNumber(phone)):
        print("[!] invalid number, skipping..".format(phone))
        fail += 1
    else:
        
        browser.get("https://web.whatsapp.com/send?phone=" + phone + "&text=" + message + "&app_absent=0")
        try:
            # locate whatsapp web send button to indicate load completion
            sentButtonElem = WebDriverWait(browser, chatLoadDelay).until(EC.presence_of_element_located((By.XPATH, '//footer//div//div//div//div//button')))
            time.sleep(1)
            # try to locate send button
            try: 
                sendButton = browser.find_element_by_xpath('//footer//div//div//div//div//button')
                sendButton.click()
                print("> message sent to " + phone + "!")
                success += 1
                time.sleep(1)
                print("> waiting for " + interval + " seconds before the next message..")
                time.sleep(int(interval))
                continue
            except NoSuchElementException:
                pass

            # try to locate invalid url modal
            try: 
                invalidElem = browser.find_element_by_xpath('//div[contains(text(), "url is invalid.")]')
                print("> [!] {} is not a valid phone number, skipping..".format(phone))
                fail += 1
                continue
            except NoSuchElementException:
                pass
            print("> [!] failed to send to {}, skipping..".format(phone))
            fail += 1
        except TimeoutException or TimeoutError:
            print("> [!] Loading took too much time for {}! (waited for {} seconds) Skipping".format(phone, chatLoadDelay))
            continue

browser.close()
print("> Finished broadcasting messages to {} numbers with {} successes and {} fails.".format(len(phones), success, fail))
input("Press Enter to quit")