word1="PQRST"

word2="ABC"

smallest_word=word1 if word1<word2 else word2

largest_word=word1 if word1>word2 else word2

merged=""

for i in range(0,len(smallest_word)):

    merged+=word1[i]+word2[i]

balance_word=largest_word[len(smallest_word):]

merged+=balance_word

print(merged)



