#Trivia Game COMP 363 Final Project
#Bhargvi Handa and Amshah Mushtaq

import random
import time

print("Welcome to the Trivia Game!")

player_name = input("Enter your name to get started: ")
player_score = 0
computer_score = 0

#This is a dictionary filled with easy marvel trivia questions and their answer choices
Marvel_easy_questions = {
    "1. How many infinity stones are there?":["ten", "six","five","two"],
    "2. In which Avengers movie do the Avengers first assemble?":["Avengers Infinity War", "Avengers Age of Ultron", "The Avengers", "Avengers Endgame"],
    "3. What gift does Peter give MJ in Spider-Man Far From Home?":["notebook","a black dahlia bracelet", "Black Dahlia Necklace", "drone"],
    "4. In Thor:Ragnarok, how long does Loki say he was falling for?":["thirty minutes", "twenty minutes", "forty minutes", "ten minutes"],
    "5. What is the name of THor's hammer?":["Peggy", "Jonathan", "Mjolnir", "Storm Breaker"]
}

#This is a dictionary filled with hard marvel trivia questions and their answer choices
Marvel_hard_questions = {
    "6. Who said this line?: “I don’t know if you’ve been in a fight before but there's usually not this much talking": ["Peter Parker/Spider-Man", "Bucky Barnes/The Winter Soldier","Steve Rogers/Captain America", "Sam Wilson/The Falcon"], 
    "7. What is Morgan's first line Avengers Endgame?:": ["Let’s go play","Define lunch or be disintegrated" ,"I am Iron Man","Hi Daddy"], 
    "8. In Spider-Man No Way Home, how does Peter trap Dr.Strange in the mirror dimension?": ["Peter webs Dr. Strange to a piece of the canyon","Peter uses his webs to create a archimedes spiral","Peter webs Dr. Strange to the train"],
    "9. Who said this line to Loki in the Disney+ series Loki?: Your job is to help others become the best versions of themselves": ["Mobius","Ravonna renslayer", "Sylvie","Hunter B-15"],
    "10. What does Tony tell Peter when he sees him being beamed up into Ebony Maw’s Q-ship?": ["Your too high up, your running out of air","But you said save the wizard","Pete, you gotta let you I’m gonna catch you", "Kid, where did you come from?"]
}

#This is a dictionary filled with easy world history questions and their answer choices
History_easy_questions = {
    "1. How many world wonders are there?": ["4","7","2","1"],
    "2. What is the tallest building in the world?": ["Willis Tower in Chicago","Burj Khalifa in Dubai","Shanghai Tower in China","One World Trade Center in New York City"],
    "3. When did World War I start?":["1928","1901","1916","1914"],
    "4. Which country had the world’s first newspaper?": ["England","United States of America","China","Canada"],
    "5. Which is the largest country in the world based on population?": ["India","United States of America","China","Indonesia"]
}

#This is a dictionary filled with hard world history questions and their answer choices
History_hard_questions = {
    "6. When was the United States Declaration of Independence signed?": ["October 15, 1776","June 19, 1775","August 2, 1776","April 9, 1777"],
    "7. What is considered the largest empire in history?": ["Han Dynasty","Mongol Empire","Ottman Empire","Russian Empire"],
    "8. What was the name of the group formed to maintain world peace after WWI?": ["League of Legends","League of World Peace","League of Nations","League of Alliance"],
    "9. The Great Pyramid was built as a tomb for which pharaoh?": ["Khufu","Neferirkare Kakai","Userkaf","Sahure"],
    "10. How many languages are estimated to be spoken around the world?": ["8000","2500","500","7100"]
}

#These dictionaries have the question numbers and their correct answers
Marvel_easy_questions_answers = {
    "1.": "six",
    "2.": "The Avengers",
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

while True:
    question_answer_pair = random.choice(list(Marvel_easy_questions.items()))


    question = question_answer_pair[0]
    answer_choices = question_answer_pair[1]
    computer_choice = random.choice(answer_choices)
    #time.sleep(5)
    print("Here is your question:", question)
    print("Here are the answer choices:")
    print("")
    print(answer_choices[0])
    print(answer_choices[1])
    print(answer_choices[2])
    print(answer_choices[3])
    player_answer = input("What is the answer?: ")
    for i in range(len(answer_choices)): #pass in list of answer choices
        if answer_choices[i] == player_answer: #conduct linear search to see if the answer choices equals the player answer then we know the choice is valid 
            print("The answer choice is valid") 
            for i in Marvel_easy_questions_answers: #loop through the Marvel_easy_questions_answers dictionary 
                if player_answer == Marvel_easy_questions_answers[i]: #check if the player answer matches the answer in the Marvel_easy_questions dictionary 
                    if computer_choice != Marvel_easy_questions_answers[i]: #if the player gets the correct answer see if the computer gets it wrong
                        player_score = player_score + 5     #player gains 5 points
                        computer_score = computer_score - 3 #computer loses 3 points
                        print("computer choice:", computer_choice)
                        print(player_name + "", "score:" , player_score) 
                        print("computer score:", computer_score)
                        break

                    if computer_choice == Marvel_easy_questions_answers[i]:  #if the player and computer both get the question right then we both get 5 points
                        computer_score = computer_score + 5
                        player_score = player_score + 5
                        print("computer choice:", computer_choice)
                        print(player_name + "", "score:" , player_score) 
                        print("computer score:", computer_score)
                        break
                
                elif player_answer != Marvel_easy_questions_answers[i]:         #now we see if the player gets a answer wrong and the computer gets it right
                    if computer_choice == Marvel_easy_questions_answers[i]:     #if the computer gets it right then the computer gets 5 points but the player loses 3 points
                        computer_score = computer_score + 5
                        player_score = player_score - 3
                        print("computer choice:", computer_choice)
                        print(player_name + "", "score:" , player_score) 
                        print("computer score:", computer_score)
                        break

                    if computer_choice != Marvel_easy_questions_answers[i]:   #but if both the computer and player get a question wrong then they both lose 3 points.
                        computer_score = computer_score - 3
                        player_score = player_score - 3
                        print("computer choice:", computer_choice)
                        print(player_name + "", "score:" , player_score) 
                        print("computer score:", computer_score)
                        break
                


                # player gets Q right, computer gets it wrong [x]
                # player gets Q rihgt, computer gets it right [x]
                # player gets Q wrong, computer gets it right
                # player gets Q wrong, computer gets it wrong




                """
                    player_score = player_score + 5
                    computer_score = computer_score + 5
                    print("computer choice:", computer_choice)
                    print(player_name + "", "score:" , player_score) 
                    print("computer score:", computer_score)
                    break
                
                elif player_answer == Marvel_easy_questions_answers[i]:
                    if computer_choice != Marvel_easy_questions_answers[i]:
                         player_score = player_score + 5
                         computer_score = computer_score - 3
                         print("computer choice:", computer_choice)
                         print(player_name + "", "score:" , player_score) 
                         print("computer score:", computer_score)
                         break
                """
                """
                elif player_answer != Marvel_easy_questions_answers[i]:
                    if computer_choice != Marvel_easy_questions_answers[i]:
                         player_score = player_score - 3
                         computer_score = computer_score - 3
                         print("computer choice:", computer_choice)
                         print(player_name + "", "score:" , player_score) 
                         print("computer score:", computer_score)
                         break

                    if computer_choice == Marvel_easy_questions_answers[i]:
                        player_score = player_score - 3
                        computer_score = computer_score + 5
                        print("computer choice:", computer_choice)
                        print(player_name + "", "score:" , player_score) 
                        print("computer score:", computer_score)
                        break
                """



                #elif player_answer != Marvel_easy_questions_answers[i]:
                 #   player_score = player_score - 2
                  #  print(player_name + "", "score:" , player_score)
                   # break 
                   
                
               
                
                #elif player_answer != Marvel_easy_questions_answers[i] and computer_choice != Marvel_easy_questions_answers[i]:
                 #   player_score = player_score - 2
                  #  computer_score = computer_score - 2
                   # print(player_name + "", "score:" , player_score) 
                    #print("computer score:", computer_score)

                
                    #if computer_choice == Marvel_easy_questions_answers[i]:
                     #   computer_score = computer_score + 1
                      #  print("computer score:", computer_score)
                       # print("score:" , player_score) 
                 

#also think about if nobody gets the question right then how do we show that?



#tasks to complete:


#2. create the cases so we can play w/ the computer. if player and computer don't get the answer right then they get 2 points off. if player gets it right but 
#computer doesn't then player gets the point. if computer gets it right but player doesn't then computer gets the points but player gets 2 points off.









                
                #elif player_answer == Marvel_easy_questions_answers[i] == computer_choice
                 #   player_score = player_score + 1
                    #computer_score = computer_score + 1
                   
                    
                

        #This part still needs some fixing. I need to check if we put in a valid answer then it goes thorugh linear search
        """
        elif player_answer != answer_choices[i]:
            player_answer = input("What is the answer?:")
            if player_answer == answer_choices[i]:
                break
            for i in range(len(answer_choices)): #pass in list of answer choices
                if answer_choices[i] == player_answer: #conduct linear search to see if the answer choices equals the player answer then we know the choice is valid 
                    print("The answer choce is valid") 
                    for i in Marvel_easy_questions_answers[i]: #loop through the Marvel_easy_questions_answers dictionary 
                        if player_answer == Marvel_easy_questions_answers[i]: #check if the player answer matches the answer in the Marvel_easy_questions dictionary 
                                player_score = player_score + 1
                                print("score:" , player_score) 
                                """
    


#linearSearch(answer_choices, player_answer)


#So, in reference to the first idea, perhaps after getting two "easy" questions right, one of the "hard" questions could be asked next to keep the user on their toes. 
#use linear search to check if the players answer is in the answer choice list
#if yes, then see if the answer matches the 'correct_answer value'
#if no, make them put in another answer
#make another dictionary where you have the question numbers as keys and then the correct answer as the value so then once we go past the linear search we check the player
#answer with that dictionary 