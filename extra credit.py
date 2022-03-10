books = float(input("Please enter the amount of books you would like to purchase.\n"))
if 1 <= books <= 9:
    print("The total cost is:",10*books)
elif 10 <= books <= 19:
    quantity = 10*books
    discount = .15*quantity
    print("The total cost is:",quantity-discount)
elif 20 <= books <= 49:
    quantity = 10*books
    discount = .25*quantity
    print("The total cost is:",quantity-discount)
elif 50 <= books <= 99:
    quantity = 10*books
    discount = .35*quantity
    print("The total cost is:",quantity-discount)
elif books >= 100:
    quantity = 10*books
    discount = .45*quantity
    print("The total cost is:",quantity-discount)
else:
    print("Error")