from CalculateGradient import *
from CalculateNewton import *
from GetUserInput import *
#According to vscode 'Import "CalculateGradient" could not be resolved', however, it works fine for me.

def Main():
    UserAnswers = [0, 0, 0, 0, 0, 0] 
    #AskUser(UserAnswers)                   
    print('Your input was: ')
    print(UserAnswers) # Just to see if everyting is ok.
    #Here we can call function to calculate F/G

    UserAnswers = ['1', 'F', '1', 2, '1', 10.0]     #Values only for the testing purposes
    if(UserAnswers[0] == '2'):
        CalculateNewton(UserAnswers[1], UserAnswers[2], UserAnswers[3], UserAnswers[4], UserAnswers[5])
    else:
        CalculateGradient(UserAnswers[1], UserAnswers[2], UserAnswers[3], UserAnswers[4], UserAnswers[5])
            
Main()
