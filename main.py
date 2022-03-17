from CalculateGradient import *
#import method
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
        if method.func == 'F':
            method.batchMode()
        else:
            method.matrixBatchMode()
    else:
        CalculateGradient(UserAnswers[1], UserAnswers[2], UserAnswers[3], UserAnswers[4], UserAnswers[5])
          
Main()
#uncomment in order to make the Newton's method work for the F function in stead of using Main() function
''' 
method = NewtonsMethod('F', '1', 2, '1', 10.0)
method.getUserInput()
method.batchMode()
'''

#Important notices
'''
0) Both teammates are currently on the Athens exchange since last friday, which make it hard to create a code on time.

1) Code crashes for non-batch mode (batch mode with iteration = 1) due to the fact that the average is being calculated for one x value only, despite the fact that there was an attempt to prevent that.
2) For the Newton's method there is a need to call the function F explicitly (as in commented part above), as otherwise the program crashes miraclously.
'''
