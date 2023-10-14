import random

run_game = True
# 1 = rock
# 2 = paper
# 3 = scissors

# Defined variables

# Score it takes to win the game
winning_score = 0
# Score the computer has
comp_score = 0
# Score the player has
player_score = 0


# Returns 0 if tied, 1 if the first player won, and 2 if second won
def rock_paper_scissors(first, second):
  if first == second:
    return 0
  else:
    if first == "rock":
      if second == "paper":
        return 2
      else:
        return 1
    if first == "paper":
      if second == "rock":
        return 1
      else:
        return 2
    if first == "scissors":
      if second == "rock":
        return 2
      else:
        return 1


# Maps number to string
def align(num):
  if num == 1:
    return "rock"
  if num == 2:
    return "paper"
  if num == 3:
    return "scissors"


# Prints the scores in a formatted string
def print_scores():
  print(f"Computer score: {comp_score}, Player score: {player_score}")


# Takes in what the game should play to
print("What will the winning score be?")
inp = int(input())
winning_score = inp

while (run_game):
  rps_self = random.randint(1, 3)
  self_str = align(rps_self)
  print("Let's play! type your number. \n1: rock \n2: paper\n3:scissors")
  inp = int(input())
  
  while (inp < 1 or inp > 3):
    print("That's an invalid response! try again")
    inp = int(input())

  print(f"I play {self_str}")
  result = rock_paper_scissors(align(rps_self), align(inp))
  if result == 1:
    comp_score += 1
    print("I won this round\n")
    
  elif result == 2:
    player_score += 1
    print("You won this round\n")
    
  else:
    print("We tied!\n")
    
  print_scores()
  print()
  
  if comp_score == winning_score:
    run_game = False
    print("Looks like I won the game. Try again")
  if player_score == winning_score:
    run_game = False
    print("Looks like you won the game. Congratulations!")
