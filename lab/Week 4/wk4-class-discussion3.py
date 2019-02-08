# This program generates a sequence of fibonacci numbers based on 2 seed values.

def fibonacci(number_front,number_back):
        # Base case
        if(number_back<1000):
            print(str(number_back))
            number_front,number_back = number_back,number_front+number_back
            
            # Generate recursion
            fibonacci(number_front,number_back)

# initialise variables
seed1 = seed2 = 1
seed1 = int(input("Input first seed value: "))
seed2 = int(input("Input second seed value: ")) 

# Get user input and run recursion
while(seed1 != -1 and seed2!= -1):
    print(seed1)
    fibonacci(seed1,seed2)
    seed1 = int(input("Input first seed value: "))
    seed2 = int(input("Input second seed value: "))  
    
print('Program has ended.')