# Program to find the smaller of three numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))


if num1 == num2 == num3:
    print("All numbers are equal.")
elif num1 <= num2 and num1 <= num3:
    print("The smaller number is:", num1)
elif num2 <= num1 and num2 <= num3:
    print("The smaller number is:", num2)
else:
    print("The smaller number is:", num3)