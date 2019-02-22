#This scripts checks the validity of a password

lowCase = False
upCase = False
digit = False
length = False

#All conditions to be satisified
while(not (lowCase and upCase and digit and length)):
    lowCase = False
    upCase = False
    digit = False
    length = False
    pw = input('Please input password: ')
    
    #Check length of password >= 8
    n = len(pw)
    if(n>=8):
        length = True
    
    #for each character check if at least 1 uppercase, lowercase & digit exists    
    for ch in pw:
        if(ch.isupper()):
            upCase = True
            
        elif(ch.islower()):
            lowCase = True        
            
        elif(ch.isdigit()):
            digit = True
            
        else:
            valid = False
            
    print('Lowercase: ', lowCase)
    print('Uppercase: ', upCase)
    print('Digit: ', digit)
    print('Length > 8: ', length)
        
print('Password is valid.')