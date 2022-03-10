#Loop version
newString=input("Enter a string:\n")
reverse=""
length=len(newString)
index=length - 1 
while index>=0:
    reverse=reverse+newString[index]
    index=index-1
print("Using Loops the reverse string is:", reverse)
#Slicing version
print("Using Slicing the reverse string is:", newString[::-1])