def Fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1 
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
        
def main():
    number=int(input("Enter a positive number:\n"))
    while number<0:
        print("Fibonacci applies to positive numbers only.")
        number=int(input("Enter a positive number:\n"))
    print('The Fibonacci of '+str(number)+"="+str(Fibonacci(number)))
    
main()