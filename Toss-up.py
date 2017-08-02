""" PROGRAMMING ASSIGNMENT-1
       TOSS UP DICE GAME

    NAME :   SUHAS SURESH
    CLASS:   CS-524-02
    DATE :   10/26/2015"""

""" Program to simulate the "TOSS UP" dice game
    Allows two players to play a game of toss up where there will be 10 dices with 3-green faces, 2-yellow faces and 1-red face
    A player will hit press any key to roll the dice and score points, the player with more points greater than 100 at the end of the game wins """

#Importing function randint from package random which is useful in generating random numbers.
from random import randint

#Defining a function to output the turn score and total score of the player.
def display(turn_score,scores,player):
    print ("Score for this turn is %d" % (turn_score))
    print ("Total Score of Player%d is %d " % (player,scores[player]))
    
"""Defining a function which takes the following parameters as input
1)Number_of_dices : placeholder of number of dices rolled each time.
2)Scores : A dictionary which stores the key value score for each player.
3)Player : Player refers to the player who is in action rolling the dice.
4)last_chance : Is a boolean value if true it is the last_chance of the player.
5)high_score : placeholder for highest score."""
def dice_roll(number_of_dices,scores,player,last_chance,high_score,turn_score):
    roll_score = 0    #refers to score of each dice roll.

    #randint function is used to obtain occurences of dices with colors green/yellow/red in random, each time dices are rolled.
    number_of_greens=randint(0,number_of_dices) #refers to number of dices with green color.
    number_of_yellows=randint(0,number_of_dices-number_of_greens) #refers to number of dices with yellow color.
    number_of_reds=number_of_dices-number_of_greens-number_of_yellows #refers to number of dices with red color.
    flag = first_chance 
    print ("You have got")
    
    print ("%d Greens" % (number_of_greens))
    print ("%d Yellows" % (number_of_yellows))
    print ("%d Reds" % (number_of_reds))
    turn_score +=number_of_greens #refers to score of each turn.
    roll_score += number_of_greens
    print ("Score for this roll is %d" % (roll_score)) #displaying the score of the current roll.
    
    

    #If there are no yellows and greens and if it is the first turn end the turn with no score, else retain the previous score.
    if number_of_greens == 0 and number_of_yellows == 0 and number_of_reds!=0:
        print("OOPS!! you have rolled all reds")
        decision = 'N'
        turn_score = 0
        
        if flag:
            scores[player] = turn_score
        else:
            scores[player]+=turn_score
        display(turn_score,scores,player) #invoking function display() to print the score of the turn and total score of player
        
    #Avoid user to make a decision to continue or not if its the last chance        
    elif last_chance:
        scores[player]+=roll_score
        display(turn_score,scores,player) #invoking function display() to print the score of the turn and total score of player
        if scores[player] <= high_score: #prompt the user to continue until current player exceeds the other player
            input("Press any key to continue!")
        decision='Y'
    else:
        scores[player]+=roll_score
        display(turn_score,scores,player) #invoking function display() to print the score of the turn and total score of player
        decision=input("Do you want to continue? Press (Y) if Yes or (N) if No. Y/N ") #To capture the decision of the user whether to continue or not?        
    number_of_dices=number_of_dices-number_of_greens   #To update the number of dices to be rolled after setting dices with green color aside. 

    
    #If it is the last chance avoid rolling of dice if the score is more than the other player.  
    if ((last_chance) and scores[player]>high_score):
        decision = 'N'
        
    #Continue rolling the dice if the player wishes to continue.
    if decision.upper() == 'Y':
    #If the score reaches 10, again start rolling from 10 dices.        
        print ("Great!! Please continue rolling the dice")
        if number_of_dices == 0:
            print ("You have 10 dices to roll")
            dice_roll(10,scores,player,last_chance,high_score,turn_score)            
        else:
            print ("You have %d dices to roll" %number_of_dices)
            dice_roll(number_of_dices,scores,player,last_chance,high_score,turn_score)

    #Shift the turn to next player if the current player wishes to discontinue.                                           
    elif decision.upper() == 'N':
        
        
        print ("End of turn for player%d" %player)


"""Start of the main function
   which invokes the dice_roll function to calculate the scores of players and
   finally declares the winner based on the scores."""
#Beginning the game with the first player
player = 1
last_chance = False  #Is a boolean value, if true it is the last_chance of the player.
first_chance = True  #Is a boolean value, if true it is the first_chance of the player.

#Defining a dictionary to store scores of two players.
scores = {'1' : '0','2' : '0'}
scores = {int(k):int(v) for k,v in scores.items()}


print ("\t\t------------------------------------------\n\n")
print ("\t\t Welcome to the game of Toss Up Dice\n")
print ("\t\t------------------------------------------\n\n")
print ("\t\tRules of the Game")
print ("\t\tYou are given with 10 dices with each having 3 green, 2 yellow and 1 red")
print ("\t\tTurn continues until you end up getting no greens and no yellows.")
print ("\t\tPlayer can decide when to end his/her turn.")
print ("\t\tPlayer with highest score greater than 100 wins the game.")
print ("\t\tDecide who wants to go first and Lets start the game")
print ("\t\tHere You Go!!!")
print ("\t\tMay the best player win")
print ("\t\tALL THE BEST!!!\n\n")

#Continue rolling the dice until the score of any player reaches more than 100.
while (scores[1]) < 100 and (scores[2])< 100:
    for player in scores:
        if scores[1] >= 100 or scores[2] > 100:
            break
        print ("Turn of Player%d" % player)
        input ("Press any key to start rolling the dice")
        print ("Here you GO!!!!")
        dice_roll(10,scores,player,last_chance,0,0)   
    first_chance = False #After completion of first turn, assigning first_chance to false signifying the end of first turn.
    
else:
#award a last chance to other player after a player scores more than 100
    last_chance = True
    if scores[1] >= 100:
        print ("This is the last chance for player2")
        print ("Please start rolling the dice")
        dice_roll(10,scores,2,last_chance,scores[1],0)       
    elif scores[2] >= 100:
        print ("This is the last chance for player1")
        print ("Please start rolling the dice")
        dice_roll(10,scores,1,last_chance,scores[2],0)
#Compare scores gained by both the player and declare the winner accordingly.
    if scores[1] > scores[2]:
        print ("Player1 wins with a score of %d" %scores[1])
        print ("Congratulations Player1!!!")
    else:
        print ("Player2 wins with a score of %d" %scores[2])
        print ("Congratulations Player2!!!")
