numb_list = [8, 2 , 4, 5 ,4, 11]
def largest_difference(nu4mb_list):
  biggest = numb_list[0]
  smallest = numb_list[0]
  for x in numb_list:
    if x == numb_list[0]:
      pass
    else:
      if biggest < x: 
        biggest = x
        pass
      else:
        pass
  for x in numb_list:
    if x == numb_list[0]:
      pass
    else:
      if smallest > x: 
        smallest = x
        pass
      else:
        pass
  return biggest-smallest
print(largest_difference(numb_list))


#Define a function named largest_difference that takes a list of numbers as its only parameter.

#Your function should compute and return the difference between the largest and smallest number in the list.

#For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.

#You may assume that no numbers are smaller or larger than -100 and 100.