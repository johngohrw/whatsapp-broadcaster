def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


        
clearConsole = lambda: print('\n' * 150)