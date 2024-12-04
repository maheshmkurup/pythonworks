text="this is a simple programming question to find words with maximum number of characters"

words=text.split(" ")

def get_length(w):

    return len(w)

print(max(words,key=get_length))


#using lambda function

gett_length=lambda w:len(w)

print(max(words,key=gett_length))


#sorting in descending order

def get_length(w):

    return len(w)

srt_words=sorted(words,key=get_length,reverse=True)

print(srt_words)


 
#using lambda

gett_length=lambda w:len(w)

print(sorted(words,key=gett_length,reverse=True))



#finding most frequent word in text

text="this is a simple programming question and it is to find words with maximum number of characters"

words=text.split(" ")

def get_count(w):

    return words.count(w)

most_frequent_word=max(words,key=get_count)

print(most_frequent_word)

