text=["apple","iphone","orange","potato"]

vow=["a","e","i","o","u"]

vowel_words=[w for w in text if w[0] in vow]

print(vowel_words)


consonent_words=[w for w in text if w[0] not in vow]

print(consonent_words)
