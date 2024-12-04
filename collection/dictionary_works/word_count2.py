words=["hello","hai","hello","this","is","this","is","hello"]

word_frequency={w:words.count(w) for w in words}

print(word_frequency)

recursive_words= [k for k,v in word_frequency.items() if v>1]

print(recursive_words)

non_recursive_words= [k for k,v in word_frequency.items() if v==1]

print(non_recursive_words)

max_frequency=max(word_frequency.values())

print(max_frequency)

most_reccursing_word={k for k,v in word_frequency.items() if v==max_frequency}

print("Most reccursing word=",most_reccursing_word)





