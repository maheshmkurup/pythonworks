sentance="Hello how are you are you happy"

words=sentance.split()

word_count={}

for word in words:

    if word in word_count:

        word_count[word]+=1

    else:

        word_count[word]=1

print(word_count) 