""" 
Create a random integer between 1 and 1000, and make me guess it.
Use error handling to make sure I enter an integer.
Tell me if I'm too high or too low.
Ask me to guess again until I get it right.
Keep a list of all of my answers.
Tell me how many tries it took, and print out my list of guesses.
BONUS: Tellme how I have narrowed down the range. For instance, if I guess 500 and that's too high, tell me that I have narrowed it to between 1 and 500. Then if I guess 250 and that's too low, tell me it is between 250 and 500. Feel free to hurl a mild insult if I guess something out of range.
"""
import random
guess_list = []
the_number = random.randint(1,1000)
def guess()
  the_guess = input("Guess my number: ")
  guess_list.pop(the_guess)
  if the_guess > the_number:
    print("That is too big.")
    print("Updated ranged: 1- %d" % the_guess)
    guess()
  elif the_guess < the_number:
    print("That is too small.")
    print("Updated ranged: %d - 1000" % the_guess)
    guess()
  else: 
    print("You got it!")
    print("It took you %d guesses" % len(guess_list))
    for item in guess_list:
      print(item)
    
      
    