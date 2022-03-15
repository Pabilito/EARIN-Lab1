import method as mt
import GetUserInput as gt

uncertainty = 0.000001

class NewtonsMethod(mt.OptimizationMethod):
    def __init__(self, func, vers, iter, stopc, stopv):
        '''
        Uses inheritance to get parameters
        '''
        super().__init__(func, vers, iter, stopc, stopv)
        
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
            print(self.GetGradientF(newX))
            if self.StopConditionMet(currentY) or float(abs(self.GetGradientF(newX))) <= float(uncertainty):
                print('Minimum found at: ('+str(currentX)+','+str(currentY)+')') 
                self.valuesX.append(currentX)
                self.valuesY.append(currentY)
                return
            else:
                currentX = newX


    def calculateMatrixMethod(self):
        '''
        Performes optimization with the Newton's method on the d dimentional set of functions
        '''
        

    def getSecondGradient(self, x):
        '''
        Gets the second order gradient of given function
        '''
        return 6*self.a * x + 2 * self.b
    

method = NewtonsMethod('F', '1', 2, '1', 10.0)
method.getUserInput()
method.batchMode()
