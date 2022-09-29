#Trivia Game COMP 363 Final Project
#Bhargvi Handa and Amshah Mushtaq (TRYING DIFFERENT APPROACH)

import random
import time

print("Welcome to the Trivia Game!")

player_name = input("Enter your name to get started: ")
player_score = 0


#This is a dictionary filled with easy marvel trivia questions and their answer choices
Marvel_easy_questions = {
    "How many infinity stones are there?":["ten", "six","five","two"],
    "In which Avengers movie do the Avengers first assemble?":["Avengers Infinity War", "Avengers Age of Ultron", "The Avengers", "Avengers Endgame"],
    "What gift does Peter give MJ in Spider-Man Far From Home?":["notebook","a black dahlia bracelet", "Black Dahlia Necklace", "drone"],
    "In Thor:Ragnarok, how long does Loki say he was falling for?":["thirty minutes", "twenty minutes", "forty minutes", "ten minutes"],
    "What is the name of THor's hammer?":["Peggy", "Jonathan", "Mjolnir", "Storm Breaker"]
}

#This is a dictionary filled with hard marvel trivia questions and their answer choices
Marvel_hard_questions = {
    "Who said this line?: “I don’t know if you’ve been in a fight before but there's usually not this much talking": ["Peter Parker/Spider-Man", "Bucky Barnes/The Winter Soldier","Steve Rogers/Captain America", "Sam Wilson/The Falcon"], 
    "What is Morgan's first line Avengers Endgame?:": ["Let’s go play","Define lunch or be disintegrated" ,"I am Iron Man","Hi Daddy"], 
    "In Spider-Man No Way Home, how does Peter trap Dr.Strange in the mirror dimension?": ["Peter webs Dr. Strange to a piece of the canyon","Peter uses his webs to create a archimedes spiral","Peter webs Dr. Strange to the train"],
    "Who said this line to Loki in the Disney+ series Loki?: Your job is to help others become the best versions of themselves": ["Mobius","Ravonna renslayer", "Sylvie","Hunter B-15"],
    "What does Tony tell Peter when he sees him being beamed up into Ebony Maw’s Q-ship?": ["Your too high up, your running out of air","But you said save the wizard","Pete, you gotta let you I’m gonna catch you", "Kid, where did you come from?"]
}

#This is a dictionary filled with easy world history questions and their answer choices
History_easy_questions = {
    "How many world wonders are there?": ["4","7","2","1"],
    "What is the tallest building in the world?": ["Willis Tower in Chicago","Burj Khalifa in Dubai","Shanghai Tower in China","One World Trade Center in New York City"],
    "When did World War I start?":["1928","1901","1916","1914"],
    "Which country had the world’s first newspaper?": ["England","United States of America","China","Canada"],
    "Which is the largest country in the world based on population?": ["India","United States of America","China","Indonesia"]
}

#This is a dictionary filled with hard world history questions and their answer choices
History_hard_questions = {
    "When was the United States Declaration of Independence signed?": ["October 15, 1776","June 19, 1775","August 2, 1776","April 9, 1777"],
    "What is considered the largest empire in history?": ["Han Dynasty","Mongol Empire","Ottman Empire","Russian Empire"],
    "What was the name of the group formed to maintain world peace after WWI?": ["League of Legends","League of World Peace","League of Nations","League of Alliance"],
    "The Great Pyramid was built as a tomb for which pharaoh?": ["Khufu","Neferirkare Kakai","Userkaf","Sahure"],
    "How many languages are estimated to be spoken around the world?": ["8000","2500","500","7100"]
}


userCategory = input("Which category do you want? Marvel(a) or History(b): ")
userLevel = input("Do you want easy(a) or hard(b) questions?: ")

if userCategory == "a" and userLevel == "a":
    #marvel and easy
    question_answer_pair = random.choice(list(Marvel_easy_questions.items()))

if userCategory == "a" and userLevel == "b ":
    #marvel and hard
    question_answer_pair = random.choice(list(Marvel_hard_questions.items()))

if userCategory == "b" and userLevel == "a":
    #history and easy
    question_answer_pair = random.choice(list(History_easy_questions.items()))



if userCategory == "b" and userLevel == "b":
    #history and hard 
    question_answer_pair = random.choice(list(History_hard_questions.items()))

while True:
    #make a loop for the questions 
    #question = question_answer_pair[0]
    #for i in range(len(question)):

    question = question_answer_pair[0]
    answer_choices = question_answer_pair[1]
    
    print("")
    print("Here is your question:", question)
    print("")
    print("Here are the answer choices:")
    print(answer_choices[0])
    print(answer_choices[1])
    print(answer_choices[2])
    print(answer_choices[3])

    player_answer = input("What is the answer?: ")
    for i in range(len(answer_choices)): #pass in list of answer choices
        if answer_choices[i] == player_answer: #conduct linear search to see if the answer choices equals the player answer then we know the choice is valid 
            print("The answer choice is valid.")
        
            file = open("/Users/amshahm/Desktop/TriviaGame/trivia_game/answers.txt")
            contents = file.read()
            searchWord = player_answer
            if searchWord in contents:
                print("Yay! You got it!")
                player_score = player_score + 5
                print(player_name + "'s Score: ") #leave as is, else there is an error 
                print(player_score) 
            else:
                print("Sorry! Wrong answer.")
            