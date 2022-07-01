#!/usr/bin/env python3
import random



while True:

   try:
       print()
       userInput = int(input("Try to guess what number I'm thinking of between 1- 5: "))
       number  = random.randint(1,5)
       print()
       if userInput > 10 or userInput < 1:
          print("You must select a number between 1 & 10")
          print()
       elif userInput == number:
          print(f"{userInput} is the correct number!")
          print()
          playAgain = input("Do you want to play again?\n")

          if playAgain.lower() == "yes" or playAgain.lower() == "y":
              continue
          else:
              break
       else:
          print("Your guessed the wrong number...")
          print()
          playAgain = input("Do you want to play again? \n")

          if playAgain.lower() == "no" or playAgain.lower() == "n":
              break
          elif playAgain.lower() == "yes" or playAgain.lower() == "y":
              continue
          else:
              break
   except:
       print("Invalid answer given")

    


