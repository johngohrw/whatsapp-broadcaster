from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver import ActionChains
from random import randint
from tkgui import runGUI
from utils import RepresentsInt, clearConsole, isValidNumber, stripNonNumeric, printArt, printInline, printReplace
from colorama import init
from colorama import Fore, Back, Style
import tkinter as tk
import time
import datetime

log = []

def writeLog(string):
    log.append(str(datetime.datetime.now()) + " - " + string + "\n")
    return string

def saveLog():
    # pass
    logName = 'broadcast-log_{}'.format(datetime.datetime.now())
    logfile = open('{}.txt'.format(logName.replace(".", "-").replace(":", "-")), 'a')
    for line in log:
        logfile.write(line)
    logfile.close()
    print("> a log is saved at {}".format(logName))


if __name__ == "__main__":
    init(autoreset=True) # init colorama
    printArt()
    print(Fore.YELLOW + "This program requires ChromeDriver to work.\n"+ Style.RESET_ALL +"You can download it here: {}https://chromedriver.chromium.org/downloads".format(Fore.CYAN))
    print("Choose the right version of ChromeDriver according to your computer's Chrome version.\nYou can check your Google Chrome version by:\n\n  Chrome's top-right menu > Help > About Google Chrome\n")
    print("Please make sure you have the right ChromeDriver file in the same directory as " + Fore.GREEN + "WhatsappBroadcaster.exe")

    returnValues = runGUI()
    clearConsole()
    phones = returnValues["phones"].split('\n')
    message = returnValues["message"].replace("\n", "%0A")
    interval = returnValues["interval"]

    if (not RepresentsInt(interval)): 
        print(Fore.RED + "Interval value is not a number, please relaunch and try again.")
        input("You may now close the window.")
        quit()

    print(writeLog("Loading Chrome webdriver.."))

    browser = webdriver.Chrome()
    browser.set_page_load_timeout(30)
    delay = 40
    whatsappLoadDelay = 30
    chatLoadDelay = 40
    QRCodeScanDuration = 6000
    clickableDelay = 10

    clearConsole()
    print(writeLog("Loading WhatsApp Web.."))

    browser.get("https://web.whatsapp.com/")

    try:
        myElem = WebDriverWait(browser, whatsappLoadDelay).until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Scan me!"]')))
        time.sleep(1)
    except TimeoutException or TimeoutError:
        browser.close()
        print(writeLog(Fore.RED + "Loading WhatsApp took too much time! (QR code scanner not found after {} seconds)".format(whatsappLoadDelay)))
        saveLog()
        input("You may now close the window.")
        quit()

    print(writeLog(Fore.CYAN + "Please scan the QR code on the WhatsApp Web screen."))

    try:
        myElem = WebDriverWait(browser, QRCodeScanDuration).until(EC.presence_of_element_located((By.XPATH, '//div[@id="pane-side"]')))
        time.sleep(1)
    except TimeoutException or TimeoutError:
        browser.close()
        print(writeLog(Fore.RED + "Took too long to scan QR code. Please do it within {} minutes)".format(whatsappLoadDelay/60)))
        saveLog()
        input("You may now close the window.")
        quit()

    print(writeLog(Fore.GREEN + "WhatsApp Login success!"))
    time.sleep(1)
    print(Fore.YELLOW + "\nPlease ensure that the Chrome window is not minimized throughout the process\nsince on-screen elements won't be detected.\n")
    time.sleep(1)

    animChars = ["Starting broadcasting in 3", ".", ". ", "2", ".", ". ", "1", ".", ". \n\n"]
    printInline(animChars[0])
    for i in range(1, len(animChars)):
        time.sleep(0.5)
        printInline(animChars[i])
    time.sleep(1)

    success = 0
    fail = 0
    # loop thru each phone number
    for number in phones:
        phone = stripNonNumeric(number)
        errorMessage = "failed to send, skipping"

        # skip if length is 1 or less
        if (len(phone) <= 1):
            continue

        preSendString = "> [" + Fore.CYAN + phone + Style.RESET_ALL + "]"
        printReplace(preSendString + " ["+ Fore.YELLOW + "SENDING"+Style.RESET_ALL+"]")
        if (not isValidNumber(phone)):
            printInline(writeLog(preSendString + Fore.RED + " [!]" + Style.RESET_ALL + " invalid number, skipping..".format(phone)))
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
                    sendButton = WebDriverWait(browser, clickableDelay).until(EC.element_to_be_clickable((By.XPATH, '//footer//div//div//div//div//button')))
                    sendButton.click()
                    printInline(writeLog(preSendString + Fore.GREEN + " [SUCCESS]\n"))
                    success += 1
                    timeToWait = int(interval)
                    for i in range(timeToWait, -1, -1):
                        printReplace("> waiting for " + str(i) + " seconds..")
                        time.sleep(1)
                    continue
                except NoSuchElementException or ElementNotInteractableException:
                    printReplace(writeLog(preSendString + Fore.YELLOW + " [CANNOT FIND SEND BUTTON]"))
                    errorMessage = "cannot find send button, skipping"
                    pass

                # try to locate invalid url modal
                try: 
                    invalidElem = browser.find_element_by_xpath('//div[contains(text(), "url is invalid.")]')
                    printInline(writeLog(preSendString + Fore.RED + " [!] " + Style.RESET_ALL + " invalid number, skipping..".format(phone)))
                    fail += 1
                    printInline("\n")
                    continue
                except NoSuchElementException or ElementNotInteractableException:
                    errorMessage = "cannot find send button or invalid URL modal, skipping"
                    pass
                printInline(writeLog(preSendString + Fore.RED + " [!] " + Style.RESET_ALL + " {}".format(errorMessage)))
                fail += 1
            except TimeoutException or TimeoutError:
                printInline(writeLog(preSendString +  Fore.RED + " [!] " + Style.RESET_ALL + "Could not locate Send button. skipping.. \n"))
                print(Fore.YELLOW + "\nIs the Chrome window minimized? On-screen elements can't be detected if it is.\n")
                time.sleep(3)
                continue
        printInline("\n")

    print(writeLog("> Finished broadcasting messages to {} numbers with {}{}{} successes and {}{}{} fails.".format(success + fail, Fore.GREEN, success, Style.RESET_ALL, Fore.RED, fail, Style.RESET_ALL)))
    saveLog()
    input("You may now close the window.")
    browser.close()