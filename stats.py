countA=countB=countC=countD=countF=0
score=int(input("Please enter a grade:\n"))
min=100 
max=0
sum=0 
while score>=0:
    sum+=score
    if score<min:
        min=score 
    if score>max:
        max=score 
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
    score=int(input("Please enter a grade:\n"))
count=countA+countB+countC+countD+countF
print("The sum of the scores is:",sum)
print("The mean of the scores is:",sum/count)
print("The lowest score is:",min)
print("The highest score is:",max)
print("The number of scores entered are:",count)
print("The number of A's=",countA)
print("The number of B's=",countB)
print("The number of C's=",countC)
print("The number of D's=",countD)
print("The number of F's=",countF)
