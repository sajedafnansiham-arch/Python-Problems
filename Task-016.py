# Swap Without Temporary Variable

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Before Swapping: num1 =", num1, "num2 =", num2)

num1, num2 = num2, num1

print("After Swapping: num1 =", num1, "num2 =", num2)