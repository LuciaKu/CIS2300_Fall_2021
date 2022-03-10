budget=float(input("Enter the amount budgeted for this month:\n"))
expense=float(input("Enter an expense or -1 to stop:\n"))
total =0

while expense!= -1:
    print("expense:", expense)
    total = total+expense
    print("total:",total)
    expense=float(input("Enter an expense or -1 to stop:\n"))
    
if total > budget:
    difference=total-budget
    print("You are",difference, "over budget")
elif total<budget:
    difference=budget-total
    print("You are",difference, "under budget")
else:
    print("You are exactly on budget")


        
    

    







    