from CalculateF import *
from CalculateG import *

line = "-------------------------------------------------------------------"

def Main():
    while(1):
        print(line)
        print('Write "F" to use: F(x) = ax^3 + bx^2 + cx + d')
        print('Write "G" to use: G(x) = c + bTx + xTAx')
        print('Write "EXIT" to exit')
        print(line)
        func = input()
        if(func == 'EXIT'):
            return
        if(func != 'F' and func != 'G'):
            "Improper input, choose again!"
            continue
        while(1): #I don't want to make user input F/G once again in case of error
            print(line)
            print('Write "1" to choose initial vector version')
            print('Write "2" to choose uniform distribution version')
            print('Write "BACK" to go back')
            print(line)
            vers = input()
            if(vers == 'BACK'):
                break
            if(vers != '1' and vers != '2'):
                "Improper input, choose again!"
                continue
            while(1): #As previously, I don't want the user to start from scratch in case of typo
                print(line)
                print('Write how many iterations (if > 1 we have a batch mode) of calculations (int)? ')
                print('Write "BACK" to go back')
                print(line)
                iter = input()
                if(iter == 'BACK'):
                    break
                try: # Is the input an int?
                    iter = int(iter)
                    if(iter<1):
                        print('There has to be at least 1 iteration, choose again!')
                        continue
                except:
                    print('Number could not be accepted, choose integer again!')
                    continue
                while(1):
                    print(line)
                    print('Choose stoping condition')
                    print('Write "1" to choose maximum number of iterations')
                    print('Write "2" to choose desired value')
                    print('Write "3" to choose maximum computation time in seconds')
                    print('Write "BACK" to go back')
                    print(line)
                    stopc = input()
                    if(stopc == 'BACK'):
                        break
                    if(stopc != '1' and stopc != '2' and stopc != '3'):
                        "Improper input, choose again!"
                        continue
                    while(1):
                        print(line)
                        print('Choose stoping value (float/int)')
                        print('Write "BACK" to go back')
                        print(line)
                        stopv = input()
                        if(stopv == 'BACK'):
                            break
                        try: # Is the input a float?
                            stopv = float(stopv)
                            if((stopv < 1 and stopc == '1') or (stopv < 0 and stopc == '2')):
                                print('There has to be at least 1 iteration and computation time cannot be negative, choose again!')
                                continue
                            #TU JESZCZE TRZEBA BĘDZIE POMYŚLEĆ CZY SĄ JAKIEŚ OGRANICZENIA DLA stopc == 2
                        except:
                            print('Number could not be accepted, choose again!')
                            continue
                        #Here we can call specific function 
                        print(line)                       
                        print('Your input was: ' + func, vers, str(iter), stopc, str(stopv) + ' \nStarting calculations.')
                        print(line)
                        if(func == "F"):
                            CalculateF(vers, iter, stopc, stopv)
                        else:
                            CalculateG(vers, iter, stopc, stopv)
                        break
                    break
                break
            break
            

try:
    Main()
except:
    print('Exception occurred. Restarting programme.') #Wiem, że to dosyć głupie.
    Main()