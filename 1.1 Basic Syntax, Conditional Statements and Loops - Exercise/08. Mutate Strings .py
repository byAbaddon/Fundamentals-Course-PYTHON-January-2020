word_one = input()
word_two = input()
collection = ''

for i in range(len(word_one)):
   if word_one[i] != word_two[i]:
      collection = word_two[0:i+1] + word_one[i+1:100]
      print(collection)

   

