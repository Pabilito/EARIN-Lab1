import numpy as np
import random
import statistics
import GetUserInput as gt
import time

class OptimizationMethod:
    '''
    The parent class of the gradient optimization methods
    '''
    def __init__(self, func, vers, iter, stopc, stopv):
        '''initializes the class'''
        self.func = func
        self.vers = vers
        self.iter = iter
        self.stopc = stopc
        self.stopv = stopv
        self.valuesX = []         #For batch mode data storage
        self.valuesY = []         #For batch mode data storage
        self.iterations = 0       #For stopping conditions
        self.execTime = 0         #For stopping conditions
        self.step = 0.01

    def getUserInput(self):
        '''
        If indicated in the variable self.func, the user input for function
        coefficients will be taken
        '''
        if self.func == 'F':
            self.a = gt.GetFloatFromUser('Write a coefficaient value [float]')
            self.b = gt.GetFloatFromUser('Write b coefficaient value [float]')
            self.c = gt.GetFloatFromUser('Write c coefficaient value [float]')
            self.d = gt.GetFloatFromUser('Write d coefficaient value [float]')
        else:
           self.c = gt.GetFloatFromUser('Write c coefficaient value [float]')
           self.d = gt.GetIntFromUser('Write d size of matrix [int]') 
           self.b = gt.GetMatrixFromUser("Please provide b (d values) [float]", self.d, 1, False)
           self.A = gt.GetMatrixFromUser("Please provide A positive-definite matrix (d x d values) [float]", self.d, self.d, True)


    def getMatrixRange(self, batchn):
        '''
        Based on vers we ask for range of the matrix. We return correct X
        '''
        if(self.vers == '1'):                        #Version with specific point
            x = gt.GetMatrixFromUser("Please provide x (d values) [float]", self.d, 1, False)
        else:
            x = gt.GetRandomizedMatrixFromUser("Please provide min (d values) [float]. Then d max values", self.d)
        return x

    def matrixBatchMode(self):
        '''
        Batch mode interface for the matrix operations
        '''
        for batchn in range(self.iter):   #Batch mode implementation - if we don't want batch mode, user can simply have iter = 1
            self.calculateMatrixMethod(batchn)


    def calculateMatrixMethod(self, batchn):
        '''
        Performes optimization with default method on the given matrix.
        '''
        x = self.getMatrixRange(batchn)
        starttime = time.time()
        self.iterations = 0
        print('Batch mode: ', (batchn+1), '/', iter)            
        while(1):
            self.execTime = time.time() - starttime
            currentY = self.c + np.matmul(np.transpose(self.b), x) + np.matmul(np.matmul(np.transpose(x), self.A), x)
            currentY = currentY.item(0)
            currentGradient = self.GetGradientG(x)
            if(self.StopConditionMet(currentY) or currentGradient.all() == 0):
                print('Minimum found at: (', x ,',', currentY, ')') 
                self.valuesX.append(x)
                self.valuesY.append(currentY)
                break
            self.iterations += 1
            #Do G function
            x = x - self.step * currentGradient #Calculate gradient for matrix and apply it
                
    def GetGradientG(self, x):
    #Derivative is b + A*x + At*x
        return (self.b + np.matmul(self.A,x) + np.matmul(np.transpose(self.A),x))
                
    def getRange(self):
        '''
        Based on vers we ask for range. We return current x.
        '''
        if(self.vers == '1'):
            currentX = gt.GetFloatFromUser('Write starting X coordinate[float]')
        else:                                   #Version with range
            currentXmin = gt.GetFloatFromUser('Write starting X minimum coordinate[float]') 
            currentXmax = gt.GetFloatFromUser('Write starting X maximum coordinate[float]')
            if(currentXmax<currentXmin):      #If somebody made a mistake and has max<min, I will not ask him again
                currentX = random.uniform(currentXmax, currentXmin)
            else:
                currentX = random.uniform(currentXmin, currentXmax)
        return currentX

    def calculateMethod(self):
        '''
        Performes optimization with default method.
        '''
        currentX = self.getRange()
        while(1):  #Apply gradient descent in an infinite loop until stopping condition is met or we are at minimum     
            currentY = self.GetY(currentX)
            #Check if we can return value
            currentGradient = self.GetGradientF(currentX)
            if(self.StopConditionMet(currentY) or currentGradient == 0):
                print('Minimum found at: ('+currentX+','+currentY+')') 
                self.valuesX.append(currentX)
                self.valuesY.append(currentY)
                break
            currentX = currentX - self.step * currentGradient #Gradient descent done here
                    
    def batchMode(self):
        '''
        Stats operating in the batchmode until user change the iter parameter
        to be equal 1
        '''
        for batchn in range(self.iter):   #Batch mode implementation - if we don't want batch mode, user can simply have iter = 1 
            self.calculateMethod()
        print('Average x is:' + statistics.mean(self.valuesX))
        print('Average y is:' + statistics.mean(self.valuesY))
        print('Stdev x is:' + statistics.stdev()(self.valuesX))
        print('Stdev y is:' + statistics.stdev()(self.valuesY))
        return 

    def GetGradientF(self, x):
        #ax^3+bx^2+cx+d
        #So derivative is 3ax^2+2bx+c
        return 3*self.a*x*x+2*self.b*x+self.c

    def StopConditionMet(self, currentY):
        if((self.stopc == '1' and self.iterations == self.stopv) or (self.stopc == '2' and currentY <= self.stopv) or (self.stopc == '3' and self.execTime >= self.stopv)):
            return True
        return False

    def GetY(self, x):
        #ax^3+bx^2+cx+d
        return self.a*x*x*x+self.b*x*x+self.c*x+self.d

'''    
method = OptimizationMethod('a', '1', 2, '1', 10.0)
method.getUserInput()
method.batchMode()
method.matrixBatchMode()
'''
