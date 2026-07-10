# Program to check voting eligibility based on age

age = int(input("Enter your age: "))

if age < 0:
    print("You are not born yet!..👶😂")
elif age >= 18:
    print("Eligible for voting..😎")
else:
    print("Not eligible for voting..🤪")