text="This is a simple python program to find the most recursive word. this program is simple"

words=text.split(" ")

get_length=lambda word:words.count(word)

most_frequent_word=max(words,key=get_length)

print(most_frequent_word)

