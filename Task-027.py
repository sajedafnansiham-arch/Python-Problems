#Bitwise Operator

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# & (AND) - Duita bit e 1 thakle result 1 hoy
print("Bitwise AND (&):", num1 & num2)

# | (OR) - Jekono ekta bit 1 hole result 1 hoy
print("Bitwise OR (|):", num1 | num2)

# ^ (XOR) - Duita bit alada hole result 1 hoy
print("Bitwise XOR (^):", num1 ^ num2)

# ~ (NOT) - Number er sob bit ulte dey
print("Bitwise NOT (~):", ~num1)

# << (Left Shift) - Bit bam dike 1 ghor soray (2 diye gun korar moto)
print("Left Shift (<<):", num1 << 1)

# >> (Right Shift) - Bit dan dike 1 ghor soray (2 diye vag korar moto)
print("Right Shift (>>):", num1 >> 1)