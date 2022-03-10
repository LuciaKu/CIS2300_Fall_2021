def B(n,k): 
    if k==0 or k==1:
        return 1 
    else:
        return  B(n-1,k-1) + B(n-1,k) 

print("The binomial coefficients for B(12,5) is:", B(12,5))
print("The binomial coefficients for B(10,7) is:", B(10,7))
print("The binomial coefficients for B(15,9) is:", B(15,9))