#program to check a character is an alphabet

chr = input("Enter a character : ")

if len(chr)==1 and (chr >= "A" and chr <= "Z") or (chr >= "a" and chr <= "z"):
    print("It is an alphabet..")

else:
    print("Its not an alphabet..")    