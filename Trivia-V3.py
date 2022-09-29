#Trivia Game COMP 363 Final Project
#Bhargvi Handa and Amshah Mushtaq (TRYING DIFFERENT APPROACH)

import random
from re import A
import time

print("Welcome to the Trivia Game!")

player_name = input("Player 1, Enter your name to get started: ")
player_score = 0
player2_name = input("Player 2, Enter your name to get started: ")
player2_score = 0


#This is a dictionary filled with easy marvel trivia questions and their answer choices
Marvel_easy_questions = {
    "How many infinity stones are there?":["a. ten", "b. six","c. five","d. two"],
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

#These dictionaries have the question numbers and their correct answers
Marvel_easy_questions_answers = {
    "1.": "b",
    "2.": "c",
    "3.": "Black Dahlia Necklace",
    "4.": "thirty minutes",
    "5.": "Mjolnir"
}

Marvel_hard_questions_answers = {
    "6.": "Sam Wilson/The Falcon",
    "7.": "Define lunch or be disintegrated",
    "8.": "Peter uses his webs to create a archimedes spiral",
    "9.": "Mobius",
    "10.": "Pete, you gotta let you I’m gonna catch you"
}

History_easy_questions_answers = {
    "1.": "7",
    "2.": "Burj Khalifa in Dubai",
    "3.": "1914",
    "4.": "China",
    "5.": "China"
}

History_hard_questions_answers = {
    "6.": "August 2, 1776",
    "7.": "Mongol Empire",
    "8.": "League of Nations",
    "9.": "Khufu",
    "10.": "7100"
}


userCategory = input("Which category do you want? Marvel(a) or History(b): ")
userLevel = input("Do you want easy(a) or hard(b) questions?: ")

if userCategory == "a" and userLevel == "a":
    #marvel and easy
    question_answer_pair = list(Marvel_easy_questions.items())

if userCategory == "a" and userLevel == "b ":
    #marvel and hard
    question_answer_pair = list(Marvel_hard_questions.items())

if userCategory == "b" and userLevel == "a":
    #history and easy
    question_answer_pair = list(History_easy_questions.items())

if userCategory == "b" and userLevel == "b":
    #history and hard 
    question_answer_pair = list(History_hard_questions.items())

questionCount = 1
while questionCount != 6:
    question = question_answer_pair[0]
    answer_choices = question_answer_pair[1]

    #make a loop for the questions 
    for question, answer_choices in Marvel_easy_questions.items(): #make sure this works for all categories
        print("")

        print("Here is your question:", question)
        print("")
        print("Here are the answer choices:")
        print(answer_choices[0])
        print(answer_choices[1])
        print(answer_choices[2])
        print(answer_choices[3])

        player_answer = input("What is the answer?: ")
        player2_answer = input("Enter your answer player 2:")
        questionCount = questionCount + 1
        for i in range(len(answer_choices)): #pass in list of answer choices
            if answer_choices[i] == player_answer: #conduct linear search to see if the answer choices equals the player answer then we know the choice is valid 
                print("The answer choice is valid.")
                for i in Marvel_easy_questions_answers: #loop through the Marvel_easy_questions_answers dictionary 
                    if player_answer == Marvel_easy_questions_answers[i]: #check if the player answer matches the answer in the Marvel_easy_questions dictionary 
                        if player2_answer != Marvel_easy_questions_answers[i]: #if the player gets the correct answer see if the computer gets it wrong
                            player_score = player_score + 5     #player gains 5 points
                            player2_score = player2_score - 3 #computer loses 3 points
                            print(player_name + "'s Score: ")
                            print(player_score) 
                            print(player2_name + "'s Score:")
                            print(player2_score)
                            break

                        if player2_answer == Marvel_easy_questions_answers[i]:  #if the player and computer both get the question right then we both get 5 points
                            player2_score = player2_score + 5 
                            player_score = player_score + 5
                            print(player_name + "'s Score: ")
                            print(player_score) 
                            print(player2_name + "'s Score:")
                            print(player2_score)
                            break
                
                    
                    elif player_answer != Marvel_easy_questions_answers[i]:         #now we see if the player gets a answer wrong and the computer gets it right
                        if player2_answer == Marvel_easy_questions_answers[i]:     #if the computer gets it right then the computer gets 5 points but the player loses 3 points
                            player2_score = player2_score + 5
                            player_score = player_score - 3
                            print(player_name + "'s Score: ")
                            print(player_score) 
                            print(player2_name + "'s Score:")
                            print(player2_score)
                            break

                        else:
                            player2_score = player2_score - 3
                            player_score = player_score - 3
                            print(player_name + "'s Score: ")
                            print(player_score) 
                            print(player2_name + "'s Score:")
                            print(player2_score)
                            break


                        """        
                        if player2_answer != Marvel_easy_questions_answers[i]:   #but if both the computer and player get a question wrong then they both lose 3 points.
                            player2_score = player2_score - 3
                            player_score = player_score - 3
                            print(player_name + "'s Score: ")
                            print(player_score) 
                            print(player2_name + "'s Score:")
                            print(player2_score)
                            break
                        """

                    #some function to bring the user back to choosing categories or exiting the game
                    #do different text files per catrgory (4 in total)
                    #organize it into functions
                    #multiplayer - edit in the end 
                