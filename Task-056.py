# Program to check an alphabet is a vowel or consonant

ch = input("Enter an alphabet: ")

if len(ch) == 1 and ch.isalpha():
    if ch in "AEIOUaeiou":
        print(f"{ch} is a vowel.")
    else:
        print(f"{ch} is a consonant.")
else: 
    print("Invalid input!")