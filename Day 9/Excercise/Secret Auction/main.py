from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

#print Gavel
print(art.logo)

#welcome message
print("Welcome to the secret auction program.")

#create a dictionary for ALL bids
bids= {}

#ask for bidder information
bidder = str(input("What is your name?"))
bid_amount = int(input("what is your bid?: $"))

bids[bidder] = bid_amount

#ask for another bidder
last_bid = str(input("Are there any other bidders: Type 'yes' or 'no'."))

#ensure last_bid is lowercase
last_bid = last_bid.lower()

while last_bid == 'yes':
  #clear console
  clear()
  
  #ask for bidder information
  bidder = str(input("What is your name?"))
  bid_amount = int(input("what is your bid?: $"))
  bids[bidder] = bid_amount

  #ask for another bidder
  last_bid = str(input("Are there any other bidders: Type 'yes' or 'no'."))

#choose highest bid in bids
auction_winner = max(bids, key=bids.get)

print(f"Winner of autcion is {auction_winner}")
