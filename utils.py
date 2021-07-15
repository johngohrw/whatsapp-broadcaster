import re

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