import random

#For aesthetic purposes.
line = "-------------------------------------------------------------------"

def GetFloatFromUser():
    while(1):
        print(line)
        print('Write starting point value (float)')
        retVal = input()
        try: # Is the input a float?
            retVal = float(retVal)
            print(line) 
            return retVal
        except:
            print('Number could not be accepted, choose again!')
            continue  

def GetGradientF(a,b,c,x):
    return 3*a*x*x+2*b*x+c

def CalculateGradient(func, vers, iter, stopc, stopv):

    if(func == 'F'):
    #ax^3+bx^2+cx+d
    #So derivative is 3ax^2+2bx+c
        
        #Based on vers we ask for range.
        if(vers == '1'):                        #Version with specific point
            initpoint = GetFloatFromUser()
        else:                                   #Version with range
            initpointmin = GetFloatFromUser() 
            initpointmax = GetFloatFromUser()
            if(initpointmax<initpointmin):      #If somebody made a mistake and has max<min, I will not ask him again
                initpoint = random.uniform(initpointmax, initpointmin)
            else:
                initpoint = random.uniform(initpointmin, initpointmax)


        print(initpoint)
        return

    else:
    #Do G function
        return

    print("Gradient")
    
    return