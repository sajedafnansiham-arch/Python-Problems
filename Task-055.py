# Program to check a character is a digit

dig = input("Enter a digit : ")

if len(dig) == 1 and dig >= '0' and dig <= '9':
    print("It is a digit.")
else:
    print("It is not a digit.")