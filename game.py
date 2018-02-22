import random

go_again = True

name = raw_input("Welcome to Rock, Paper, Scissors! What's your name? ").title()
print

while go_again == True:
  playerChoice = raw_input("Hey, " + name.title() + "!" + " Rock, Paper or Scissors? ").title()
  computerChoice = random.randint(1,3)

  if computerChoice == 1:
  	computerChoice = "Rock"
  elif computerChoice == 2:
  	computerChoice = "Paper"
  else:
  	computerChoice = "Scissors"
  	
  print

  print playerChoice + " vs " + computerChoice

  if playerChoice == computerChoice:
    print "Draw!"
    outcome = 0
  elif playerChoice.lower() == "rock" and computerChoice.lower() == "paper":
    print "Computer Wins!"
    outcome = 2
  elif playerChoice.lower() == "rock" and computerChoice.lower() == "scissors":
    print name + " Wins!"
    outcome = 1
  elif playerChoice.lower() == "paper" and computerChoice.lower() == "rock":
    print name + " Wins!"
    outcome = 1
  elif playerChoice.lower() == "paper"and computerChoice.lower() == "scissors":
    print "Computer Wins!"
    outcome = 2
  elif playerChoice.lower() == "scissors" and computerChoice.lower() == "rock":
    print "Computer Wins!"
    outcome = 2
  elif playerChoice.lower() == "scissors" and computerChoice.lower() == "paper":
    print name + " Wins!"
    outcome = 1
  else:
    print "Oops! Something didn't work quite right. Try running the script again!"

  print

  if outcome == 0:
    again = raw_input("Ooh, close! Wanna have another go? ").lower()
    if again == "no" or again == "n":
      print
      print "Thanks for playing, " + name + "."
      go_again = False
    else:
      print
  elif outcome == 1:
    again = raw_input("Congratualtions, you won! Willing to try again? ").lower()
    if again == "no" or again.l() == "n":
      print
      print "Thanks for playing, " + name + "."
      go_again = False
    else:
      print
  elif outcome == 2:
    again = raw_input("Aw man, the computer bet you! Better luck next time. Up for another game? ").lower()
    if again == "no" or again == "n":
      print
      print "Thanks for playing, " + name + "."
      go_again = False
    else:
      print
