from CalculateGradient import *
from CalculateNewton import *
from GetUserInput import *
#According to vscode 'Import "CalculateGradient" could not be resolved', however, it works fine for me.

#For aesthetic purposes.
line = "-------------------------------------------------------------------"

def Main():
    UserAnswers = [0, 0, 0, 0, 0, 0] 
    AskUser(UserAnswers)                   
    print('Your input was: ')
    print(UserAnswers) # Just to see if everyting is ok.
    print(line)
    #Here we can call function to calculate F/G
    if(UserAnswers[0] == '2'):
        CalculateNewton(UserAnswers[1], UserAnswers[2], UserAnswers[3], UserAnswers[4], UserAnswers[5])
    else:
        CalculateGradient(UserAnswers[1], UserAnswers[2], UserAnswers[3], UserAnswers[4], UserAnswers[5])
            
try:
    Main()
except:
    print('Exception occurred. Restarting programme.') #Wiem, że to dosyć głupie.
    Main()