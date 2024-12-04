def most_frequent_word(text):
 
 words=text.split(" ")
 
word_count={}
 
for w in word_count:
  
  if w in word_count:
   
   word_count[w]+=1

  else:
   
   word_count[w]=1

print(word_count)

most_frequent_character=max(word_count,key=word_count)

print(most_frequent_character)

text="Hello world! Hello everyone. Welcome to world."

most_frequent_word(text)