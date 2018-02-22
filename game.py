import random

go_again = True
score = 0
name = raw_input("Welcome to the game of Log, Fire, Water! What's your name? ").title()
affirm = raw_input("Would you like to set a target score? ").lower()

if affirm == "yes" or affirm == "y":
  goal = raw_input("What score would you like to reach? ")
  
print

while go_again == True:
  playerChoice = raw_input("Hey, " + name.title() + "!" + " Log, Fire or Water? ").title()
  computerChoice = random.randint(1,3)

  if computerChoice == 1:
  	computerChoice = "Log"
  elif computerChoice == 2:
  	computerChoice = "Fire"
  else:
  	computerChoice = "Water"
  	
  if playerChoice == "L" or playerChoice == "Log":
  	playerChoice = "Log"
  elif playerChoice == "F" or playerChoice == "Fire":
  	playerChoice = "Fire"
  elif playerChoice == "W" or playerChoice == "Water":
  	playerChoice = "Water"
  else:
    playerChoice = "null"
  
  if playerChoice != "null":
    print
    print playerChoice + " vs " + computerChoice

  if playerChoice == computerChoice:
    print "Draw! That was a close one."
    print
  elif playerChoice == "Log" and computerChoice == "Fire":
    score -= 1
    print "Aw man, you lost! Better luck next time."
    print
  elif playerChoice == "Log" and computerChoice == "Water":
    score += 1
    print "Congratulations, " + name + ". You won!"
    print
  elif playerChoice == "Fire" and computerChoice == "Log":
    score += 1
    print "Congratulations, " + name + ". You won!"
    print
  elif playerChoice == "Fire" and computerChoice == "Water":
    score -= 1
    print "Aw man, you lost! Better luck next time."
    print
  elif playerChoice == "Water" and computerChoice == "Log":
    score -= 1
    print "Aw man, you lost! Better luck next time."
    print
  elif playerChoice == "Water" and computerChoice == "Fire":
    score += 1
    print "Congratulations, " + name + ". You won!"
    print
  else:
    print
    print "Oops! That's not an option. You can pick from Log, Fire or Water. Try again."
    print
    go_again = True

  if affirm == "yes" or affirm == "y":
    if int(score) == int(goal):
      again = raw_input("Congratulations, you beat the computer. Want to try better your score? ").lower()
      if again == "no" or again == "n":
        print
        print "That's a shame! Thanks for playing, " + name + "."
        go_again = False
      else:
        print
    elif -3 < score < goal:
      print "Your score is " + str(score) + ". Get a score of " + str(goal) + " to win!"
      print
    elif score == -3:
      again = raw_input("Unlucky, the computer beat you. Want to get your revenge? ").lower()
      if again == "no" or again == "n":
        print
        print "That's a shame! Thanks for playing, " + name + "."
        go_again = False
      else:
        print
  else:
    go_again = True
