from CalculateGradient import *
from NewtonMethod import *
from GetUserInput import *
#According to vscode 'Import "CalculateGradient" could not be resolved', however, it works fine for me.

def Main():
    UserAnswers = [0, 0, 0, 0, 0, 0] 
    AskUser(UserAnswers)                   
    print('Your input was: ')
    print(UserAnswers) # Just to see if everyting is ok.
    #UserAnswers = ['2', 'G', '1', 2, '1', 10.0]     #Values only for the testing purposes

    #Here we can call function to calculate F/G
    if(UserAnswers[0] == '2'):
        method = NewtonsMethod(UserAnswers[1], UserAnswers[2], UserAnswers[3], UserAnswers[4], UserAnswers[5])
        method.getUserInput()
        method.matrixBatchMode()
    else:
        CalculateGradient(UserAnswers[1], UserAnswers[2], UserAnswers[3], UserAnswers[4], UserAnswers[5])
          
Main()
