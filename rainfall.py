number=[] 
for x in range (1,13):
    rainfall=float(input("How many times has it rained in month "+str(x)+"?:\n"))
    number.append(rainfall)
print("The highest rainfall is:",max(number))
print("The lowest rainfall is:",min(number))
print("The total number of rainfalls this year is:",sum(number))
print("The average number of rainfalls is:",sum(number)/len(number))