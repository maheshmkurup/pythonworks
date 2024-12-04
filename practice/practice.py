
text="this is a simple programming question and it is to find words with maximum number of characters"

words=text.split(" ")

def get_length(w):

   return len(w)

maxchar=max(words,key=get_length)

print(maxchar)