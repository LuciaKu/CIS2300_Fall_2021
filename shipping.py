weight = float(input("Please enter the weight of the item in pounds.\n"))

if 0 < weight < 5:
    shipping = input("Do you want regular or overnight shipping?\n")

    if shipping == "regular":
        print ("The item costs $7.")
    elif shipping == "overnight":
        print ("The item costs $15.")
    else:
        print ("error")

elif 5 < weight < 10:
    shipping = input ("Do you want regular or overnight shipping?\n")
    
    if shipping == "regular":
        print ("The item costs $14.")
    elif shipping == "overnight":
        print ("The item costs $25.")
    else:
        print ("error")

elif weight > 10: 
    shipping = input ("Do you want regular or overnight shipping?\n")
    
    if shipping == "regular":
        print ("The item costs $20.")
    elif shipping == "overnight":
        print ("The item costs $40.")
    else:
        print ("error")

