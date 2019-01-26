import random

players = ["Isaac", "Mike", "Claire"]

quiz_questions =[
                ["What is CEOP?", "I/ Criminal Exploration and Online Protection", "C/ Child Exploitation and Online Protection", "I/ Child Exploitation and Organised Protectors"],
                ["When you get an email from someone you do not know what should you do?", "I/ Open it and reply to them   ", "I/ Open it and click the links   ", "C/  Do not open it and delete it "],
                ["When an online contact who frightens you asks to meet you in person what should you do?", "C/ Call the police  ", "I/ Accept the invite  ", "I/ Reveal your address  "],
                ["If an email asks you to enter your bank account details because of a problem with your account what should you do?", "I/ Enter your bank details  ", "I/ Ask someone to enter their details  ", "C/ Mark the Email as Spam  "],
                ["If an email is sent to you, telling you that you have won something, what should you do?", "I/ Click on a link there   ", "I/ Tell everyone and forward the message   ", "C/ Ignore and Mark as Spam  "],
                ["Which of these passwords are safe?", "I/ lol123  ", "C/ L0l123   ", "I/ LoL   "],
                ["How can you tell if an email is a fake or phishing email, sent to trick you into giving away personal information?", "I/ It will have links in i  ", "I/   ", "C/ It asks you to do something you wouldn’t otherwise do, such as respond with your username, full password and credit card details	  "],
                ["Which of these is a telltale sign that a website isn't real, and is in fact designed to trick you into giving away your private information?", "I/ The link will go nowhere (give you a 404)  ", "I/ The email looks less professional than you expect  ", "C/ The website address looks unusual  "],
                ["How should you protect your wireless network from eavesdroppers and possible freeloaders?", "C/ Don't broadcast your SSID or the name of your network  ", "C/ Use encryption   ", "C/ Only let known computers connect to your access point   "],
                ]

numberOfQuestions = len(quiz_questions) # This part counts how many question there is
pointsPerQuestion = 3 # This is how many points per question

level = 1

def new_player():
    global playerName
    validName = False
    while validName == False:
        playerName = input ("\n Please enter your player name: ")
        for name in players: # Here we are checking to see if the name is presented above
            if playerName == name:
                validName = True
        if validName == False:
            print("This name is not registered. Try again.")

        else:
            print(" Hello", playerName, " - Best of luck on the quiz! \n")
            print("Here are the rules of the game ")
            print("-" * 40)
            print("You will be asked a series of questions about Online Safety. \n You need to read the questions carefully and answer them. \n Each question is worth 3 points by the end all your score will be totaled up.")

def quiz():
    questionsAsked = []
    # This will store the questions that have already been asked so they are not used again

    global score
    score = 0
    questionNumber = random.randint (0, numberOfQuestions - 1) # This bunch of codes from questionNumber up to questionsAsked.appened(questionNumber) turn the questions into numbers 
    while len (questionsAsked) < numberOfQuestions:
        while questionNumber in questionsAsked:
            questionNumber = random.randint(0, numberOfQuestions - 1)
            # This bolck of code check to see if the question has been used already
            # and selects another if it needs to
        questionsAsked.append(questionNumber)

        question = quiz_questions[questionNumber]

        correctAnswer = ""
        print("")
        print(question[0])
        print("")
        for i in range (1, 4):
            if question[i][0] == "C":
                # This line identifies the correct answer
                correctAnswer = i
            print (i, question[i][2:])
        print("") # There is blank space between the lines

        chosenAnswer = ""   # It checks if the number entered is not equal to 1, 2 or 3. It checks if the number enetred is correct or incorrect
        while chosenAnswer != "1" and chosenAnswer != "2" and chosenAnswer != "3":
            chosenAnswer = input("Please enter 1, 2 or 3: ")
        chosenAnswer = int(chosenAnswer)
        print("")
        if chosenAnswer == correctAnswer:
            print("This is the correct answer.")
            score +=3
        else:
            print("This is incorrect. The correct answer is : ", question[correctAnswer][2:])
            

def result():
    print("-" *40)
    print("")
    print("That is the end of the quiz.\n")
    print(playerName, " reached level ", level , " and scored ", score, " out of ", numberOfQuestions * pointsPerQuestion, "points.\n")

print("")       # This part of the code starts to join all the code togrther
print("Welcome to the Online Safety Quiz")
print("-" * 40)
new_player()
anotherGo = "Y" or "N"
while anotherGo == "Y" or anotherGo == "y":
    quiz()
    result()
    anotherGo = input("Another go(Y/N)? ")
    
print("Thanks for playing. Goodbye!")
