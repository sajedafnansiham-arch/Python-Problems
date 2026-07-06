#Membership Operator (in, not in)

fruits = ["apple", "banana", "mango", "grapes"]

fruit = input("Enter a fruit name: ").lower()

print(fruit,"is available in the list of fruits :", fruit in fruits)
print(fruit,"is not available in the list of fruits :",fruit not in fruits)