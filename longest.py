largest=0
longest=""
for x in range(1,11):
    y=input("Please enter word "+str(x)+":\n")
    if len(y)>largest:
        largest = len(y)
        longest=y 

print("The longest word is:",longest)