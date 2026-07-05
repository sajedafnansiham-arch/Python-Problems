# Swap Using Temporary Variable

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Before Swap:")
print("First Number =", num1)
print("Second Number =", num2)

temp = num1
num1 = num2
num2 = temp

print("After Swap:")
print("First Number =", num1)
print("Second Number =", num2)