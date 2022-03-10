def menu():
    print("Menu:\n"
    "1. Choice 1: Convert Gallons to Pints\n"
    "2. Choice 2: Convert Gallons to Ounces\n"
    "3. Choice 3: Convert Gallons to Liters\n"
    "4. Choice 4: Exit the Program")

def pints(gallon):
    return gallon * 8 

def ounces(gallon):
    return gallon * 128
    
def liters(gallon):
    return gallon * 3.7854
    
def select(convert, gallon):
    if convert==1:
        print("Your measure in Pints is: ")
        return pints(gallon)
    elif convert==2:
        print("Your measure in Ounces is: ")
        return ounces(gallon)
    elif convert==3:
        print("Your measure in Liters is: ")
        return liters(gallon)

name = input("What is your name?\n")

print("Welcome ",name," to the Metric Units Converter Application.")

def main():
    convert=0
    while convert!=4:
        menu()
        convert=int(input("Please select a number from the Menu, 1-4\n"))
        if convert==1 or convert==2 or convert==3:
            gallon=int(input("Please enter your measure in Gallons.\n"))
            if gallon > 0:
                result = select(convert, gallon)
                print(result)
            else:
                print("Please enter a positive number.")
        elif convert!= 1 and convert!=2 and convert!=3 and convert!=4:
            print("That is not an option.")
        else:
            print("Exiting...")
            print("Thank you for using the Metric Units Converter Application.")
 
main()
    