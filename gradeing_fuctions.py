import random

def letter_from_number(number_grade): #filtering out letter grades and returning the character associated with it
  if number_grade < 60:
    letter_output = "F"
  elif number_grade < 70:
    letter_output = "D"
  elif number_grade < 80:
    letter_output = "C"
  elif number_grade < 90:
    letter_output = "B"
  else:
    letter_output = "A"
  return letter_output

def list_average(ls_of_ints):
  input_sum = 0
  for element in ls_of_ints:
    input_sum += element
  average_output = input_sum/len(ls_of_ints); #average should work for lists of arbitrary length using len()
  return average_output

def generate_grades():
  grade_list = []
  for x in range(6):
    if x != 5: # format for the first five grades needs to be distinct from the average format
      value = random.randint(50, 100)
      grade_list.append(value)
      letter_grade = letter_from_number(value)
      print("Grade {x}: {value} {letter_grade}".format(x=x+1, value=value, letter_grade=letter_grade))
    else:
      average_value = list_average(grade_list)
      letter_grade = letter_from_number(average_value)
      print("Average: {average_value} {letter_grade}".format(average_value=average_value, letter_grade=letter_grade))
  return grade_list #return the grade list for further use in other functions if needed
generate_grades() # calling my driver function 

