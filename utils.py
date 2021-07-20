import re
from colorama import init
from colorama import Fore, Back, Style

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


        
clearConsole = lambda: print('\n' * 150)


def isValidNumber(number):
    if (len(number) <= 7):
        return False
    if (number[0] == '0'):
        return False
    return True


def stripNonNumeric(string):
    return re.sub('[^0-9]+', '', string)


def printArt():
    print("")
    print("░██╗░░░░░░░██╗██╗░░██╗░█████╗░████████╗░██████╗░█████╗░██████╗░██████╗░")
    print("░██║░░██╗░░██║██║░░██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗")
    print("░╚██╗████╗██╔╝███████║███████║░░░██║░░░╚█████╗░███████║██████╔╝██████╔╝")
    print("░░████╔═████║░██╔══██║██╔══██║░░░██║░░░░╚═══██╗██╔══██║██╔═══╝░██╔═══╝░")
    print("░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║░░░██║░░░██████╔╝██║░░██║██║░░░░░██║░░░░░")
    print("░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░")
    print("██████╗░██████╗░░█████╗░░█████╗░██████╗░░█████╗░░█████╗░░██████╗████████╗")
    print("██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝")
    print("██████╦╝██████╔╝██║░░██║███████║██║░░██║██║░░╚═╝███████║╚█████╗░░░░██║░░░")
    print("██╔══██╗██╔══██╗██║░░██║██╔══██║██║░░██║██║░░██╗██╔══██║░╚═══██╗░░░██║░░░")
    print("██████╦╝██║░░██║╚█████╔╝██║░░██║██████╔╝╚█████╔╝██║░░██║██████╔╝░░░██║░░░")
    print("╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░")
    print("")
    print("                             " + Fore.CYAN + "John Rengwu")
    print("                         "  + Fore.MAGENTA + "https://rengwu.tech")
    print("")

def printInline(string):
    print(string, end="")

def printReplace(string):
    print(string, end="\r")