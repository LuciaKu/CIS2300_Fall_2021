age = float(input("Please enter your age\n"))

if age<18:
    print("You are too young to vote")
else:
    registered = input("Have you registered to vote yet? Please enter yes or no\n")
    
    if registered == "yes":
        print("You can vote")
    elif registered == "no":
        print("You need to register before you can vote")
    

    