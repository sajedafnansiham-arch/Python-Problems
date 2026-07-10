# Program to check an alphabet is Uppercase or Lowercase

ch = input("Enter an alphabet: ")

if 'A' <= ch <= 'Z':
    print(f" \"{ch}\" is a Uppercase Alphabet")
elif 'a' <= ch <= 'z':
    print(f" \"{ch}\" is a Lowercase Alphabet")
else:
    print("Invalid Input")