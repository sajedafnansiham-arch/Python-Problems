# program to check pass or fail on exams

marks = int(input("Enter your marks : "))

if marks < 0 or marks > 100 :
    print("Invailed marks..")

elif marks >= 33 and marks <= 100 :
    print("You are passed..😎👀")    

else:
    print("You are failed..🐸🤣")    