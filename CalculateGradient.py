import random
import time
from GetUserInput import *
import statistics
import numpy as np

def GetGradientF(a, b, c, x):
    #ax^3+bx^2+cx+d
    #So derivative is 3ax^2+2bx+c
    return 3*a*x*x+2*b*x+c

def StopConditionMet(stopC, stopV, iterations, execTime, currentY):
    if((stopC == '1' and iterations == stopV)
    or (stopC == '2' and currentY <= stopV)
    or (stopC == '3' and execTime >= stopV)):
        return True
    return False

def GetY(a, b, c, d, x):
    #ax^3+bx^2+cx+d
    return a*x*x*x+b*x*x+c*x+d

def CalculateGradient(func, vers, iter, stopc, stopv):
    step = 0.01 #The lower the vale the more precise the calculations, but the longer execution time.
            #Requirements do not say that it has to be provided by the user.
    currentY = 0         #For stopping conditions
    valuesX = []         #For batch mode data storage
    valuesY = []         #For batch mode data storage

    if(func == 'F'):
        a = GetFloatFromUser('Write a coefficaient value [float]')
        b = GetFloatFromUser('Write b coefficaient value [float]')
        c = GetFloatFromUser('Write c coefficaient value [float]')
        d = GetFloatFromUser('Write d coefficaient value [float]')       
        for batchn in range(iter):   #Batch mode implementation - if we don't want batch mode, user can simply have iter = 1 
            starttime = time.time()
            iterations = 0
            print('Batch mode: ', (batchn+1), '/', iter)     
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
                execTime = time.time() - starttime
                print(currentX, currentY)
                if(StopConditionMet(stopc, stopv, iterations, execTime, currentY) or currentGradient == 0):
                    print('Minimum found at: (',currentX,',',currentY,')') 
                    valuesX.append(currentX)
                    valuesY.append(currentY)
                    break
                currentX = currentX - step * currentGradient #Gradient descent done here
                iterations += 1
        print('Average x is: ', statistics.mean(valuesX))
        print('Average y is: ', statistics.mean(valuesY))
        print('Stdev x is: ', statistics.stdev(valuesX))
        print('Stdev y is: ', statistics.stdev(valuesY))
        return 

    else:
        c = GetFloatFromUser('Write c coefficaient value [float]')
        d = GetIntFromUser('Write d size of matrix [int]')
        x = GetMatrixFromUser("Please provide x (d values) [float]", d, 1)
        print(x)
    #Do G function
        return

    print("Gradient")
    
    return