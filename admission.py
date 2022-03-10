name = input ("Please enter the student's name:\n")
GPA = float(input("What is their GPA?\n"))
testScore = float(input("What is their test score?\n"))

def AcceptOrReject(GPA,testScore):
    if GPA < 3 and testScore < 80:
        print("Student is rejected.")
    elif GPA >= 3 and testScore < 60:
        print("Student is rejected.")
    else:
        print("Student is accepted.")

AcceptOrReject(GPA,testScore)