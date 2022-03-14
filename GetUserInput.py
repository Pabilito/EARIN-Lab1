import numpy as np
#For aesthetic purposes
line = "-------------------------------------------------------------------"

def GetMatrixFromUser(message, rows, columns):
    mat = np.matrix([])
    print(line)
    print(message)
    print(line)
    for i in range(rows):
        for j in range(columns):
            tempMat = np.matrix([])
            print('Please write value for cell: [', i, '][', j, ']')
            while(1):
                val = input()
                try: # Is the input a float?
                    val = float(val)
                    break 
                except:
                    print('Number could not be accepted, choose again!')
                continue
            np.append(tempMat, val, axis = 1)
        np.append(mat, tempMat)
        tempMat.delete()
    return mat

def GetIntFromUser(message):
    while(1):
        print(line)
        print(message)
        retVal = input()
        try: # Is the input a float?
            retVal = int(retVal) 
            return retVal
        except:
            print('Number could not be accepted, choose again!')
            continue

def GetFloatFromUser(message):
    while(1):
        print(line)
        print(message)
        retVal = input()
        try: # Is the input a float?
            retVal = float(retVal) 
            return retVal
        except:
            print('Number could not be accepted, choose again!')
            continue

def Step0(UserAnswers):
    while(1): #I want to allow user to run this program multiple times
        print(line)
        print('Write "1" to use Gradient Descent Method')
        print('Write "2" to use Newtons method')
        print('Write "EXIT" to exit')
        print(line)
        meth = input()
        if(meth == 'EXIT'):
            quit() #Exit program
        if(meth != '1' and meth != '2'):
            "Improper input, choose again!"
            continue
        break
    UserAnswers[0] = meth
    return

def Step1(UserAnswers):
    while(1): 
        print(line)
        print('Write "F" to use: F(x) = ax^3 + bx^2 + cx + d')
        print('Write "G" to use: G(x) = c + bTx + xTAx')
        print(line)
        func = input()
        if(func != 'F' and func != 'G'):
            "Improper input, choose again!"
            continue
        break
    UserAnswers[1] = func
    return

def Step2(UserAnswers):
    while(1): #I don't want to make user input F/G once again in case of error
        print(line)
        print('Write "1" to choose initial vector/value version')
        print('Write "2" to choose uniform distribution version')
        print(line)
        vers = input()
        if(vers != '1' and vers != '2'):
            "Improper input, choose again!"
            continue
        break
    UserAnswers[2] = vers
    return

def Step3(UserAnswers):
    while(1): #As previously, I don't want the user to start from scratch in case of typo
        print(line)
        print('Write how many iterations (if > 1 we have a batch mode) of calculations (int)? ')
        print(line)
        iter = input()
        try: # Is the input an int?
            iter = int(iter)
            if(iter<1):
                print('There has to be at least 1 iteration, choose again!')
                continue
        except:
            print('Number could not be accepted, choose integer again!')
            continue  
        break  
    UserAnswers[3] = iter
    return

def Step4(UserAnswers):
    while(1):
        print(line)
        print('Choose stoping condition')
        print('Write "1" to choose maximum number of iterations')
        print('Write "2" to choose desired value')
        print('Write "3" to choose maximum computation time in seconds')
        print(line)
        stopc = input()
        if(stopc != '1' and stopc != '2' and stopc != '3'):
            "Improper input, choose again!"
            continue
        break
    UserAnswers[4] = stopc
    return

def Step5(UserAnswers):
    while(1):
        print(line)
        print('Choose stoping value (float)')
        print(line)
        stopv = input()                     
        try: # Is the input a float?
            stopv = float(stopv)
            if((stopv < 1 and UserAnswers[4] == '1') or (stopv < 0 and UserAnswers[4] == '2')): #Additional condition checking
                print('There has to be at least 1 iteration and computation time cannot be negative, choose again!')
                continue
            break
            #TU JESZCZE TRZEBA BĘDZIE POMYŚLEĆ CZY SĄ JAKIEŚ OGRANICZENIA DLA stopc == 2
        except:
            print('Number could not be accepted, choose again!')
            continue
    UserAnswers[5] = stopv
    return     

def AskUser(UserAnswers):
    state = 0
    numberOfQuestions = 6
    while(state < numberOfQuestions):
        if(state == 0):
            Step0(UserAnswers)
        elif(state == 1):
            Step1(UserAnswers)
        elif(state == 2):
            Step2(UserAnswers)        
        elif(state == 3):
            Step3(UserAnswers)
        elif(state == 4):
            Step4(UserAnswers) 
        elif(state == 5):
            Step5(UserAnswers)
        state+=1
    return