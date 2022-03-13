import random

#For aesthetic purposes
line = "-------------------------------------------------------------------"
step = 0.01 #The lower the vale the more precise the calculations, but the longer execution time.
            #Requirements do not say that it has to be provided by the user.
iterations = 0       #For stopping conditions
execTime = 0         #For stopping conditions
currentY = 0         #For stopping conditions
valuesX = []         #For batch mode data storage
valuesY = []         #For batch mode data storage

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

def GetGradientF(a, b, c, x):
    #ax^3+bx^2+cx+d
    #So derivative is 3ax^2+2bx+c
    return 3*a*x*x+2*b*x+c

def StopConditionMet(stopC, stopV):
    if((stopC == '1' and iterations == stopV)
    or (stopC == '2' and currentY <= stopV)
    or (stopC == '3' and execTime >= stopV)):
        return True
    return False

def GetY(a, b, c, d, x):
    #ax^3+bx^2+cx+d
    return a*x*x*x+b*x*x+c*x+d

def CalculateGradient(func, vers, iter, stopc, stopv):

    if(func == 'F'):
        a = GetFloatFromUser('Write a coefficaient value [float]')
        b = GetFloatFromUser('Write b coefficaient value [float]')
        c = GetFloatFromUser('Write c coefficaient value [float]')
        d = GetFloatFromUser('Write d coefficaient value [float]')
        for batchn in range(iter):   #Batch mode implementation - if we don't want batch mode, user can simply have iter = 1 
            print('Batch mode: ' + (batchn+1) + '/' + iter)     
            #Based on vers we ask for range.
            if(vers == '1'):                        #Version with specific point
                currentX = GetFloatFromUser('Write starting X coordinate[float]')
            else:                                   #Version with range
                currentXmin = GetFloatFromUser('Write starting X minimum coordinate[float]') 
                currentXmax = GetFloatFromUser('Write starting X maximum coordinate[float]')
                if(currentXmax<currentXmin):      #If somebody made a mistake and has max<min, I will not ask him again
                    currentX = random.uniform(currentXmax, currentXmin)
                else:
                    currentX = random.uniform(currentXmin, currentXmax) 
                while(1):  #Apply gradient descent in an infinite loop until stopping condition is met or we are at minimum     
                    currentY = GetY(a, b, c, d, currentX)
                    #Check if we can return value
                    currentGradient = GetGradientF(a, b, c, currentX)
                    if(StopConditionMet(stopc, stopv) or currentGradient == 0):
                        print('Minimum found at: ('+currentX+','+currentY+')') 
                        valuesX.append(currentX)
                        valuesY.append(currentY)
                        continue
                    currentX = currentX - step * currentGradient #Gradient descent done here
        #CALCULATE MEAN AND STD DEVIATION HERE !!!!!!!!!   
        return 

    else:
    #Do G function
        return

    print("Gradient")
    
    return