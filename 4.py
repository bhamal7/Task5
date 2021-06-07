username = 'b'

password = 'B'

userInput = input("What is your username?\n")

if userInput == username:
    for i in range(3):
        a=input("Enter your Password?\n")   
        if a == password:
            print("Welcome!")
            break
        else:
            print("That is the wrong password. Enter again")
else:
    print("That is the wrong username.")