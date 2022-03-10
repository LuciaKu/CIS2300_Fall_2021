#Pratical Final Review: Calculator Program
def menu():
    print('Menu\n'
          '1:Addition\n'
          '2:Subtraction\n'
          '3:Multiplication\n'
          '4:Division\n'
          '5:Exit\n')

#The Addition function
def add(number1,number2):
    return number1+number2

#The Subtraction function
def subtract(number1,number2):
    return number1-number2

#The Multiplication function
def multiply(number1,number2):
    return number1*number2

#The division function
def divide(number1,number2):
    if number2!=0:
        return number1/number2
    else:
        number2=int(input('Impossible to divide by Zero, please Enter a different number\n'))
        return number1/number2            

def select(operation,number1,number2):
    if operation==1:
        return add(number1,number2)
    elif operation==2:
        return subtract(number1,number2)
    elif operation==3:
        return multiply(number1,number2)
    elif operation==4:
        return divide(number1,number2)

def main():
    operation=0
    while operation!=5:
        menu()
        operation=int(input('Enter a choice from the Menu 1-5\n'))
        if operation!=5:
            number1=int(input('Enter the first number:\n'))
            number2=int(input('Enter the second number:\n'))
            result=select(operation,number1,number2)
            print('The result is:',result)
        else:
            print('Exiting....')
            print('Thank you for using my Python Calculator Program')
        
    
main()







    
