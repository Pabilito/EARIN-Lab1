#For aesthetic purposes
line = "-------------------------------------------------------------------"

def GetFloatFromUser(message):
    while(1):
        print(line)
        print(message)
        retVal = input()
        try: # Is the input a float?
            retVal = float(retVal)
            print(line) 
            return retVal
        except:
            print('Number could not be accepted, choose again!')
            continue  