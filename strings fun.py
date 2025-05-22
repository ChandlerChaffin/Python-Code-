input_sentence = input("Enter a sentnce.")
vowels = 'aeiouAEIOU'
output_sentence = ""
for letter in input_sentence: 
  if letter in vowels:
    output_sentence += letter.upper()
  else:
    output_sentence += letter.lower()
print(output_sentence)
seperated_words = []
seperated_words = input_sentence.split()
for word in seperated_words:
  if len(word) == 3:
    print(word)

  