#declaration of variables
counter = 0
countA=countB=countC=countD=countF=0
#read the first score from the user
score=int(input('Enter a grade:\n'))
while score>=0:
    if 90 <= score <= 100:
        countA+=1 
    elif score >= 80:
        countB+=1 
    elif score >= 70:
        countC+=1 
    elif score >= 60:
        countD+=1 
    else:
        countF+=1 
    score=int(input('Enter a grade:\n'))
    #end of the while loop

count=countA+countB+countC+countD+countF
#display the outputs
print("The number of scores entered were:",count)
print("A's=",countA)
print("B's=",countB)
print("C's=",countC)
print("D's=",countD)
print("F's=",countF)