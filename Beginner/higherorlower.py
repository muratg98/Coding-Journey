from game_data import data
#from art import logo, vs
import random

#Get two random datas to start with (cant be the same)
#present the data name, desc, country
#user inputs A or B to guess which one has higher follower count
#if user guess correct, the second comparison (B) becomes A and a new random B value emerges
#things I need:
#1. function to get a random data that cannot be the same as A or B
#2. function to check the followercount of both data
#3. check which followercount is higher
#4. if user guesses correct, score goes up, if not, game ends & display final score

def follower_check(data):
  followers = data['follower_count']
  return followers

score = 0
A = random.choice(data) #returns the dictionary of the account -> name, fcount, desc, location
B = random.choice(data)
while A == B:             #makes sure A and B are never the same data/accounts
  B = random.choice(data)
print("Welcome to a game of Higher or Lower!")
print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}")

def swap():
  global A, B
  C = B
  A = C
  B = random.choice(data)
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
  print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}")

playing = True
while playing:
  guess = input("Who has more followers? Type 'a' or 'b': ")
  if guess == 'a' and follower_check(A) > follower_check(B):
    score += 1
    print(f"You're Right! Current Score: {score}.")
    swap()
  elif guess == 'a' and follower_check(A) < follower_check(B):
    print(f"That was wrong. Final Score: {score}.")
    ## Game ends here
  elif guess == 'b' and follower_check(B) > follower_check(A):
    score += 1
    print(f"You're Right! Current Score: {score}.")
    swap()
  elif guess == 'b' and follower_check(B) < follower_check(A):
      print(f"That was wrong. Final Score: {score}.")
    ## Game ends here
  else:
    print("That was not a valid input.")
    continue
