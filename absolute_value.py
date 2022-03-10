def absolute_value(num):
    if num>=0:
        return num
    else:
        return -num

def main():
    number=int(input('Enter a Number\n'))
    print('The Absolute value is',absolute_value(number))

main()
    
