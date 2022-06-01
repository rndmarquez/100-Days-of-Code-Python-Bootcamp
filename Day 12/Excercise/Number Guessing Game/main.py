#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import *
import art

#define variable
attempts = 0

#make_guess
#takes user input as thier guess
def make_guess():
  try:
    guess = int(input("Make a guess: "))
  except ValueError:
    print("Guess must be an integer. Please enter an integter")
    guess = make_guess()
  return guess

def compare_guess(userGuess):
  if userGuess > myNumber:
    print("Too High\nGuess again.")
    userGuess = make_guess()
  if userGuess < myNumber:
    print("Too Low\nGuess again.")
    userGuess = make_guess()
  if userGuess == myNumber:
    print("Correct!")

#Create function that will get user input for difficulty level
#  and ensure it is within choics of easy or hard
def get_diffLevel():
  #choices = ["easy", "hard"]
  #validDiffLevel = False
  diffLevel = input("Choose a difficulty.  Type 'easy' or 'hard': ")
  
  #while not validDiffLevel:
  #  while (diffLevel != "easy") or (diffLevel != "hard"):
  #    diffLevel = input("Choose a difficulty.  Type 'easy' or 'hard': ")
  #    
  #  validDiffLevel = True
  return diffLevel

    
    

  

#TODO: Welcome the player
print(art.logo)
print("Welcome to the Number Guessing Game!")

#TODO: Tell user you are thinking of a number between 1-100. Pick a number between 1-100
print("I'm thinking of a number between 1 and 100.")
myNumber = randint(1,100)
print(myNumber)

#TODO: Ask user which level of difficulty level
diffLevel = get_diffLevel()
print(f"You chose the {diffLevel} difficulty level")

#TODO: Ensure user enters diffuclty
#TODO: easy is 10 attempts, hard is 5 attempts

if diffLevel == 'easy':
  attempts = 10
elif diffLevel =='hard':
  attempts = 5
print(f"You have {attempts} attempts")

#TODO: ask user to make a guess and check if it the correct answer
userGuess = make_guess()
attempts -= 1
while attempts != 0:
  if userGuess > myNumber:
    compare_guess(userGuess)
    attempts -= 1
  if userGuess < myNumber:
    compare_guess(userGuess)
    attempts -= 1
  if userGuess == myNumber:
    compare_guess(userGuess)
    attempts =0

print(f"The number was {myNumber}")
