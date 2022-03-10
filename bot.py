def total_invoice(price,quantity):
    if quantity < 5:
        return price*quantity
    elif 5 <= quantity <= 15:
        total=price*quantity
        discount=0.09*total
        return total-discount
    else:
        total=price*quantity
        discount=0.15*total
        return total-discount
def main():
    price=float(input("Enter the price of the item:\n"))
    quantity=float(input("Enter how many of that item you want:\n"))
    print("The total invoice is: $"+str(total_invoice(price,quantity)))
    
main()