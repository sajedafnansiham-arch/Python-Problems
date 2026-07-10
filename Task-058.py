# Program to check whether three sides can form a triangle

# Formula : 1. a + B > c,2) a + c > b , 3) b + c > a

side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))

if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print("Triangle can be formed.")
else:
    print("Triangle cannot be formed.")
