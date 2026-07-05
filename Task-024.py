#Logical Operator
marks = int(input("Enter your marks: "))

print("Passed with A+ :", marks >= 80 and marks <= 100)
print("Need Improvement :", marks < 40 or marks > 100)
print("Not Failed :", not(marks < 40))