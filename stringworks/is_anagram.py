source_word="silent"

target_word="listen"

is_anagram=True

for ch in target_word:

    if ch not in source_word:

        is_anagram=False

        break

print(is_anagram)



