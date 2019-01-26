print("Welcome to the ELI Game!")
print("Please enter your age, gender, email address and your player name.")
age = int(input("How old are you?"))

while age <= 18:
    print("Please re-enter your age.")
    age = int(input("How old are you?"))


length = False
while length == False:
    playername = input("What is your player name? (It must be more than 4 characters) " )
    if len(playername)  >= 4:
        length = True
        print("Thank you for entering your player name.")
        

#this asks them to input their details. It then collects the information and stores it.

contaivalue = False
while contaivalue == False:
    email = input("Please enter your email address: ")
    for i in range(len(email)):
        if email[i] == "@" and ".":
            contaivalue = True

#this verifys if it is an email. An email normally has an @ symbol and a dot symbol.

gender = input("Are you a Male or a Female?")



print(playername)
print(age)
print(gender)
print(email)

#this shows all the information which was given before.

answer = input("Is this the correct information? Please respond Y or N ")
if answer !="Y" or "y" or " y" or " Y":
    print("Please enter your age, gender, email address and your player name.")
    age = int(input("How old are you?"))
    gender = input("Are you a male or female?")
    playername = input("What is your player name?")
    email = input("Please enter your email address: ")
    answer = input("Have you entered your information correct this time? Please respond Y or N")
else:
        print("Thanks for confirming your details.")

#this asks them to confirm their details.
