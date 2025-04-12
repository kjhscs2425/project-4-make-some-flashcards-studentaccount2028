#We need to fix historical.txt to tell the score of historical data
#If we have time create a log in system

# Write your code here
import random

#Opening Statement
print("Welcome to the flashcard game! This game is a simple composition of difficult riddles. All riddles that you do not complete will be redirected into the next cycle. Your statistics and file data will be stored and available for your viewing. Good luck! \n")

#3 different flashcard sets to randomize order
flashcards = {
    "What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?": "A river",
    "What has a neck but no head?": "A bottle",
    "I’m tall when I’m young, and I’m short when I’m old. What am I?": "A candle",
    "Where does today come before yesterday?": "The Dictionary",
    "What month of the year has 28 days?": "It's not February, it's all of them.",
    "What is always in front of you but can’t be seen?": "The Future",
    "What can you break, even if you never pick it up or touch it?": "A Promise",
    "A man who was outside in the rain without an umbrella or hat didn’t get a single hair on his head wet. Why?": "He was bald",
    "What can’t talk but will reply when spoken to?": "An Echo",
    "I’m light as a feather, yet the strongest person can’t hold me for five minutes.": "Breath",
    "What has a head and a tail but no body?": "A Coin",
    "Where does one wall meet the other wall?": "On the corner",
    "What has a thumb and four fingers, but it is not a hand?": "A glove",
    "What building has the most stories?": "The library",
    "What tastes better than it smells?": "Your tongue",
    "What kind of coat is best put on wet?": "A coat of paint",
    "What has hands but can't clap?": "A clock",
    "What kind of band never plays music?": "A rubber band",
    "What is cut on a table but is never eaten": "A deck of cards",
    "What has words, but never speaks?": "A book",
    "What runs all around a backyard, yet never moves?": "A fence",
    "What can travel all around the world without leaving its corner?": "A stamp"
}

while True:

    #Difference between stats.txt and historical.txt is that stats.txt only tracks from the last round. Historical.txt tracks historically but only tracks write vs wrong statistic
    false_questions = []
    f = open('stats.txt', 'r')
    g = open('historical.txt', 'a')
    readfile = f.readlines()
    f.close()
    if len(readfile) > 0:
        print(readfile[-1] + " was your score last round")
    else:
        print("Last rounds score could not be found \n")
    f = open('stats.txt', 'w+')
    for item in readfile:
        if item[0] == "F":
            false_questions.append(item[2:-1])

    flashcard_keys = list(flashcards.keys())
    random.shuffle(flashcard_keys)

    #Finds if the user input is correct or incorrect and has a score at the end
    correct_score = 0
    incorrect_score = 0

    if len(readfile) > 0:
        user_question = input("Hi user! Would you like to be shown only the flashcards you haven't completed? Please respond with either a (t) for True or a (f) for False \n")
    else:
        user_question = "f"
    if user_question == "t":
        to_use = false_questions
    else:
        to_use = flashcard_keys
    for key in to_use:
        user_answer = input(key)
        user_answer = user_answer.lower()
        correct = flashcards[key]
        correct = correct.lower()
        if user_answer in correct:
            print("Correct ✅")
            correct_score+=1
            
            f.write("C|" + key + "\n")
        else:
            print("Incorrect ❎")
            print("The correct answer was: " + correct)
            incorrect_score += 1
            f.write("F|" + key + "\n")
        print("Next Question! ")

    f.write(str(correct_score) + " correct")
    g.write(str(correct_score) + " correct")
    g.write(" ")
    f.write(" ")
    f.write(str(incorrect_score) + " incorrect")
    g.write(str(incorrect_score) + " incorrect")
    winrate = correct_score/len(to_use)
    g.write(" ")
    g.write("This rounds winrate: " + str(round(winrate*100, 1)) + "%")
    g.write("\n")

    f.close()
    g.close()
    g = open('historical.txt', 'r')
    cool_file = g.read()
    g.close()
    print("Your historical data:")
    print(cool_file)
