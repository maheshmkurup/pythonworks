def count_vowels(string):

    vowels="aeiou"

    return sum(1 for ch in string if ch in vowels)

print(count_vowels("hello world"))
