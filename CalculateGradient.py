import random
import time
from GetUserInput import *
import statistics
import numpy as np

def GetGradientF(a, b, c, x):
    #ax^3+bx^2+cx+d
    #So derivative is 3ax^2+2bx+c
    return 3*a*x*x+2*b*x+c

def GetGradientG(b, A ,x):
    #Derivative is b + A*x + At*x
    return (b + np.matmul(A,x) + np.matmul(np.transpose(A),x))

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
                if(StopConditionMet(stopc, stopv, iterations, execTime, currentY) or currentGradient == 0):
                    print('Minimum found at: (',currentX,',',currentY,')') 
                    valuesX.append(currentX)
                    valuesY.append(currentY)
                    break
                currentX = currentX - step * currentGradient #Gradient descent done here
                iterations += 1
            if(iter>=2):   #to avoid calculations for non-batch mode
                print('Average x is: ', statistics.mean(valuesX))
                print('Average y is: ', statistics.mean(valuesY))
                print('Stdev x is: ', statistics.stdev(valuesX))
                print('Stdev y is: ', statistics.stdev(valuesY))
        return 

    else:
        c = GetFloatFromUser('Write c coefficaient value [float]')
        d = GetIntFromUser('Write d size of matrix [int]') 
        b = GetMatrixFromUser("Please provide b (d values) [float]", d, 1, False)
        A = GetMatrixFromUser("Please provide A positive-definite matrux (d x d values) [float]", d, d, True)

        for batchn in range(iter):   #Batch mode implementation - if we don't want batch mode, user can simply have iter = 1 
            if(vers == '1'):                        #Version with specific point
                x = GetMatrixFromUser("Please provide x (d values) [float]", d, 1, False)
            else:
                x = GetRandomizedMatrixFromUser("Please provide min (d values) [float]. Then d max values", d)
            starttime = time.time()
            iterations = 0
            print('Batch mode: ', (batchn+1), '/', iter)     
            #Based on vers we ask for range.
            while(1):
                execTime = time.time() - starttime
                currentY = c + np.matmul(np.transpose(b), x) + np.matmul(np.matmul(np.transpose(x), A), x)
                currentY = currentY.item(0)
                currentGradient = GetGradientG(b,A,x)
                if(StopConditionMet(stopc, stopv, iterations, execTime, currentY) or currentGradient.all() == 0):
                    print('Minimum found at: (', x ,',', currentY, ')') 
                    valuesX.append(x)
                    valuesY.append(currentY)
                    break
                iterations += 1
                #Do G function
                x = x - step * currentGradient #Calculate gradient for matrix and apply it 
            if(iter>=2):   #to avoid calculations for non-batch mode
                print('Average x is: ', statistics.mean(valuesX))
                print('Average y is: ', statistics.mean(valuesY))
                print('Stdev x is: ', statistics.stdev(valuesX))
                print('Stdev y is: ', statistics.stdev(valuesY))
        return
