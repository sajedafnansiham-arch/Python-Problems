#program to determine grade based on marks

marks = float(input("Enter your marks : "))

if marks < 0 or marks > 100 :
    print("Invailed marks")

elif marks >= 80:
    print("Grade : A+")
elif marks >= 70 :
    print("Grade : A ")
elif marks >= 60 :
    print("Grade : A-") 
elif marks >= 50 :
    print("Grade : B")
elif marks >= 40 :
    print("Grade : C") 
elif marks >= 33 :
    print("Grade : D") 

else:
    print("Grade : F & You are failed..🐸🤣")       

