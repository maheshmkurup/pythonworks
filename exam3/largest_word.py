def longest_word(text):
 
 words=text.split(" ")

 max_word=max(words,key=len)

 print(f"The longest word is:{max_word}")
   
longest_word("hello world! This is a test for finding longest word")



      