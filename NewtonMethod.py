import method as mt
import numpy as np
import GetUserInput as gt
import time

uncertainty = 0.001

class NewtonsMethod(mt.OptimizationMethod):
    def __init__(self, func, vers, iterek, stopc, stopv):
        '''
        Uses inheritance to get parameters
        '''
        super().__init__(func, vers, iterek, stopc, stopv)

        
    def calculateMethod(self):
        '''
        Performes optimization with the Newton's method
        '''
        currentX = self.getRange()
        while(1):
            currentY = self.GetY(currentX)
            firstDerivative = self.GetGradientF(currentX)
            secondDerivative = self.getSecondGradient(currentX)
            newX = currentX - (firstDerivative / secondDerivative)
            if self.StopConditionMet(currentY) or float(abs(self.GetGradientF(newX))) <= float(uncertainty):
                print('Minimum found at: ('+str(currentX)+','+str(currentY)+')') 
                self.valuesX.append(currentX)
                self.valuesY.append(currentY)
                return
            else:
                currentX = newX

    def calculateMatrixMethod(self, batchn):
        '''
        Performes optimization with the Newton's method on the d dimentional set of functions
        '''
        x = self.getMatrixRange(batchn)
        starttime = time.time()
        self.iterations = 1
        print('Batch mode: ', (batchn+1), '/', self.iterations)            
        while(1):
            self.execTime = time.time() - starttime
            currentY = self.c + np.matmul(np.transpose(self.b), x) + np.matmul(np.matmul(np.transpose(x), self.A), x)
            firstGradient = self.GetGradientG(x)
            secondGradient = self.GetSecondGradientG(x)
            newX = x - np.matmul(np.linalg.inv(secondGradient), firstGradient)
            currentGradient = self.GetGradientG(newX)
            if(self.StopConditionMet(currentY) or currentGradient.all() == 0):
                print('Minimum found at: (', x ,',', currentY, ')') 
                self.valuesX.append(x)
                self.valuesY.append(currentY)
                break
            else:
                x = newX
            self.iterations += 1

    def getSecondGradient(self, x):
        '''
        Gets the second order gradient of given function
        '''
        return 6*self.a * x + 2 * self.b
    
    def GetSecondGradientG(self, x):
    #Derivative is b + A*x + At*x
        return (np.transpose(self.A) + self.A)

'''
method = NewtonsMethod('a', '1', 2, '1', 10.0)
method.getUserInput()
method.batchMode()
method.matrixBatchMode()
'''
