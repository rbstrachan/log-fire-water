import random

go_again = True
score = 0
name = raw_input("Welcome to a game of Log, Fire, Water! What's your name? ").title()
goal = raw_input("\nWhat score would you like to beat? ")
print

while go_again == True:
  playerChoice = raw_input("Hey, " + name.title() + "!" + " Log, Fire or Water? ").title()
  computerChoice = random.randint(1,1)

  if computerChoice == 1:
  	computerChoice = "Log"
  elif computerChoice == 2:
  	computerChoice = "Fire"
  else:
  	computerChoice = "Water"
  	
  if playerChoice.lower() == "l" or playerChoice.lower() == "log":
  	playerChoice = "Log"
  elif playerChoice.lower() == "f" or playerChoice.lower() == "fire":
  	playerChoice = "Fire"
  elif playerChoice.lower() == "w" or playerChoice.lower() == "water":
  	playerChoice = "Water"
  else:
    playerChoice = "null"
  	
  print
  print playerChoice + " vs " + computerChoice

  if playerChoice.lower() == computerChoice.lower():
    print "Draw! That was a close one."
    print
  elif playerChoice.lower() == "log" and computerChoice.lower() == "fire":
    score -= 1
    print "Aw man, you lost! Better luck next time."
    print
  elif playerChoice.lower() == "log" and computerChoice.lower() == "water":
    score += 1
    print "Congratulations, " + name + ". You won!"
    print
  elif playerChoice.lower() == "fire" and computerChoice.lower() == "log":
    score += 1
    print "Congratulations, " + name + ". You won!"
    print
  elif playerChoice.lower() == "fire" and computerChoice.lower() == "water":
    score -= 1
    print "Aw man, you lost! Better luck next time."
    print
  elif playerChoice.lower() == "water" and computerChoice.lower() == "log":
    score -= 1
    print "Aw man, you lost! Better luck next time."
    print
  elif playerChoice.lower() == "water" and computerChoice.lower() == "fire":
    score += 1
    print "Congratulations, " + name + ". You won!"
    print
  else:
    print
    print "Oops! That's not an option. You can pick from Log, Fire or Water. Try again."
    print
    go_again = True

  if goal == "" or goal == str(0):
    go_again = True
  else:
    if -3 < score < goal:
      print "Your score is " + str(score) + ". Get a score of " + str(goal) + " to win!"
      print
    elif score == goal:
      again = raw_input("Congratulations, you beat the computer. Want to try better your score? ").lower()
      if again == "no" or again == "n":
        print
        print "That's a shame! Thanks for playing, " + name + "."
        go_again = False
    elif score == -3:
      again = raw_input("Unlucky, the computer beat you. Want to get your revenge? ").lower()
      if again == "no" or again == "n":
        print
        print "That's a shame! Thanks for playing, " + name + "."
        go_again = False
