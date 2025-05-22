import random
guess_list = []
the_number = random.randint(1,1000)
upper_limit = 1000
lower_limit = 1
def guess():
  global upper_limit 
  global lower_limit
  while True:
    try:
      the_guess = int(input("Guess my number: "))
      break
    except:
      print("Enter INTEGERS only please")
  guess_list.append(the_guess)
  if the_guess > the_number:
    print("That is too big.")
    upper_limit = the_guess
    print("Updated range: {} - {}".format(lower_limit, upper_limit))
    guess()
  elif the_guess < the_number:
    print("That is too small.")
    lower_limit = the_guess
    print("Updated range: {} - {}".format(lower_limit, upper_limit))
    guess()
  else: 
    print("You got it!")
    print("It took you {} guesses".format(len(guess_list)))
    for item in guess_list:
      print(item)
guess()
  
  
