def non_recursive_words(text):

    words=text.split(" ")

    word_count={w:words.count(w) for w in words }

    non_recursive_words={w for w in word_count if words.count(w)==1}

    print(non_recursive_words)

non_recursive_words("Hello world This is a test Hello everyone")



