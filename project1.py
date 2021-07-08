#Task 1: Write functions paymentHistory, fundsOwed, creditHistory, numRejected, annualIncome to calculate point of each factor.
#you need to add the necessary parameters for each function
def paymentHistory():
    ph = input("Payment History (enter yes or no): ")
    if(ph == "yes"):
        FPoints1 = 100
    else:
         FPoints1 = 0
    return(FPoints1)

def fundsOwed():
    fo = eval(input("Enter the amount of funds owed: "))
    if(fo == 0):
        FPoints2 = 100
    elif(1 <= fo <= 999):
        FPoints2 = 80
    elif(1000 <= fo <= 4999):
        FPoints2 = 30
    else:
         FPoints2 = 0
    return(FPoints2)
    

def creditHistory():
    ch = eval(input("Enter length of credit history; "))
    if(0 <= ch < 11):
        FPoints3 = 0
            
    elif(12 <= ch <= 47):
        FPoints3 = 80
            
    else:
         FPoints3 = 100
    return(FPoints3)

def numRejected():
    nr = eval(input("Enter number of loan applications rejected: "))
    if(nr == 0):
        FPoints4 = 100
    elif(1 <= nr <= 4):
        FPoints4 = 50
    else:
         FPoints4 = 0
    return(FPoints4)

def annualIncome():
    ai = eval(input("Enter annual income: "))
    if(0 <= ai <= 4999):
        FPoints5 = 0
    elif(5000 <= ai <= 9999):
        FPoints5 = 50
        
    else:
         FPoints5 = 100
    return(FPoints5)



#What should makeDecision do:
#1) Read the factors of a new application from the user.
#2) Calculate the points of each factor.
#3) Using the factor points and the weights, calculate the credit score.
#4) Using the threshold and the credit score return whether the application is ACCEPTED or REJECTED
 
#PARAMETERS:
#1)w1: weight for factor 1, Type: float
#2)w2: weight for factor 2, Type: float
#3)w3: weight for factor 3, Type: float
#4)w4: weight for factor 4, Type: float
#5)w5: weight for factor 5, Type: float
#6)threshold: credit score acceptance threshold, Type: float
#RETURNS:decision: the final decision, Type: string, either 'ACCEPTED' or 'REJECTED'

def makeDecision():
    print('\nReading Application\n')
#Task 2: Inside the function makeDecision: Read the factors of a new application from the user.
   
    w1 = 0.1
    w2 = 0.25
    w3 = 0.15
    w4 = 0.3
    w5 = 0.2
    threshold = 50 
    
   
    
    
    

#Task 3: Inside the function makeDecision: Calculate the points of each factor by calling corresponding functions.
    FPoints1 = paymentHistory()
    FPoints2 = fundsOwed()
    FPoints3 = creditHistory()
    FPoints4 = numRejected()
    FPoints5 = annualIncome()
    


    creditScore = (FPoints1 * w1) + (FPoints2 * w2) + (FPoints3 * w3) + (FPoints4 * w4) + (FPoints5 * w5)

    if(creditScore <= 50):
         print("Decision: REJECTED")
    else:
         print("Decision: ACCEPTED")
     


    
def main():
    #Weights and threshold are given below.
   
    
    
 
    #Task 4: Inside the function main: Read form the user the number of applications (n).
    n = eval(input("Enter the number of applications: "))     
	
    #Task 5: Inside the function main: Loop n times, in each iteration call the function makeDecision, then print decision returned by the function.
    for i in range(n):
        makeDecision()
        
    
    

   

main()
