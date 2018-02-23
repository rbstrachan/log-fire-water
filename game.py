import random
import time

go_again = True
score = 0
turns = 0
name = input("Welcome to the game of Log, Fire, Water!\nIn this variation of Rock, Paper, Scissors;\nLog bridges Water;\nWater defeats Fire; and\nFire burns Log.\nTo start, tell me, what's your name? ").title()
affirm = input("\nNice to meet you, " + name.title() + "." + " Would you like to set yourself a target score? ").lower()

if affirm == "yes" or affirm == "y":
  goal = input("\nOk, great. What score would you like to reach? ")
  print("\nGreat! " + str(goal) + " seems like a reasonable goal. Every time you win a game of Log, Fire, Water! your score will increase by 1. If you lose a game, your score will decrease by 1. Draws do not affect your score. If your score reaches " + str(goal) + ", you'll win and the game will end. If, however, your score reaches -3, the computer will win. You'll have the option to claim your revenge if you so wish. Enjoy!\n\nStarting game...")
  time.sleep(19)
  
time.sleep(1)
print("\n" * 60)

while go_again == True:
  playerChoice = input("Your turn to play, " + name.title() + "!" + " Log, Fire or Water? ").title()
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
    print()
    print(playerChoice + " vs " + computerChoice)

  if playerChoice == computerChoice:
    print("Draw! That was a close one.")
    print()
  elif playerChoice == "Log" and computerChoice == "Fire":
    score -= 1
    print("Aw man, you lost! Better luck next time.")
    print()
  elif playerChoice == "Log" and computerChoice == "Water":
    score += 1
    print("Congratulations, " + name + ". You won!")
    print()
  elif playerChoice == "Fire" and computerChoice == "Log":
    score += 1
    print("Congratulations, " + name + ". You won!")
    print()
  elif playerChoice == "Fire" and computerChoice == "Water":
    score -= 1
    print("Aw man, you lost! Better luck next time.")
    print()
  elif playerChoice == "Water" and computerChoice == "Log":
    score -= 1
    print("Aw man, you lost! Better luck next time.")
    print()
  elif playerChoice == "Water" and computerChoice == "Fire":
    score += 1
    print("Congratulations, " + name + ". You won!")
    print()
  else:
    print()
    print("Oops! That's not an option. You can pick from Log, Fire or Water. Try again.")
    print()
    go_again = True

  turns += 1
  time.sleep(2)
  print("\n" * 60)
  
  if affirm == "yes" or affirm == "y":
    if int(score) == int(goal):
      again = input("Congratulations, you beat the computer. Want to try better your score? ").lower()
      if again == "no" or again == "n":
        time.sleep(1)
        print("\n" * 60)
        print("That's a shame! Thanks for playing, " + name + ".")
        go_again = False
      else:
        score = 0
        time.sleep(1)
        print("\n" * 60)
    elif -3 < int(score) < int(goal):
      print("Your score is " + str(score) + ". Get a score of " + str(goal) + " to win!")
      print()
    elif score == -3:
      again = input("Unlucky, the computer beat you. Want to get your revenge? ").lower()
      if again == "no" or again == "n":
        time.sleep(1)
        print("\n" * 60)
        print("That's a shame! Thanks for playing, " + name + ".")
        go_again = False
      else:
        score = 0
        time.sleep(1)
        print("\n" * 60)
  else:
    if turns % 5 == 0 and turns != 0:
      interested = input("You've played " + str(turns) +  " games! Want to continue playing? ").lower()
      if interested == "yes" or interested == "y":
        go_again = True
      else:
        go_again = False
    else:
      go_again = True
