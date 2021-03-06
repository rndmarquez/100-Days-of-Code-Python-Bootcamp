#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#initialize list
choiceLetters = []
choiceSymbols = []
choiceNumbers = []

#get random letters
for i in range(0, nr_letters):
  choiceLetters.append(random.choice(letters))

#get random symbols
for j in range(0, nr_symbols):
  choiceSymbols.append(random.choice(symbols))

#get random numbers
for k in range(0, nr_numbers):
  choiceNumbers.append(random.choice(numbers))

#combine all list  to a single list
password = choiceLetters + choiceSymbols + choiceNumbers

#shuffle choices
random.shuffle(password)

#join all contents of list into a single string
password = "".join(password)
print(password)
