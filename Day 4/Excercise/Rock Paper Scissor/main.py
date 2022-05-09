import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
#Ask the player their choice for rock, papaer, scissor
playerChoice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

#test
print(playerChoice)

#pick random computer choice
comChoice = random.randint(0,2)

#test 
print (comChoice)

#translate choice to rock, paper, scissors
if comChoice == 0:
  comChoice = "Rock"
elif comChoice == 1:
  comChoice = "Paper"
else: 
  comChoice = "Scissors"

if playerChoice == 0:
  playerChoice = "Rock"
elif playerChoice == 1:
  playerChoice = "Paper"
else: 
  playerChoice = "Scissors"

#lets compare 
#Rock (0) wins against scissors(2).
#Scissors(2) win against paper(1).
#Paper(1) wins against rock(0). 

#check for draw
if playerChoice == comChoice:                                         #check for draw
  print(f"Draw, you both chose {playerChoice}, please play again")
elif playerChoice == "Rock" and comChoice == "Scissors":                #check for rock beats scissors
  print(f"{playerChoice} beats {comChoice}, you win!")
  print(rock + " BEATS "+ scissors)
elif comChoice == "Rock" and playerChoice == "Scissors":
  print(f"{comChoice} beats {playerChoice}, computer win!")
  print(rock + " BEATS "+ scissors)
elif playerChoice == "Scissors" and comChoice == "Paper":             #check for scissors beats paper
  print(f"{playerChoice} beats {comChoice}, you win!")
  print(scissors+ " BEATS "+ paper)
elif comChoice == "Scissors" and playerChoice == "Paper": 
  print(f"{comChoice} beats {playerChoice}, computer win!")
  print(scissors+ " BEATS "+ paper)
elif playerChoice == "Paper" and comChoice == "Rock":                 #check for paper beats rock
  print(f"{playerChoice} beats {comChoice}, you win!")
  print(paper +" BEATS "+ rock)
elif comChoice == "Paper" and playerChoice == "Rock": 
  print(f"{comChoice} beats {playerChoice}, computer win!")
  print(paper +" BEATS "+ rock)

