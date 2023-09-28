from replit import clear
#only works on replit ^^
from art import logo
print(logo)
print("Welcome to the secret auction program")

other_bidders = True

while other_bidders:
  name = input("What is your name?: ")
  bid = input("What's your bid?: $")
  try:
    bid = int(bid)
  except:
    print("please enter a numeric value")
    bid = input("What's your bid?: $")
  otherbids = input("Are there any other bidders? Type 'yes' or 'no'")
  if otherbids == 'no':
    other_bidders = False
  elif otherbids == 'yes':
    clear()

bidders = {}
bidders[name] = bid

highest_bidder = None
highest_bid = None

for key, value in bidders.items():
  if highest_bidder == None and highest_bid == None:
    highest_bidder = key
    highest_bid = value
  elif highest_bid < value:
    highest_bidder = key
    highest_bid = value

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")