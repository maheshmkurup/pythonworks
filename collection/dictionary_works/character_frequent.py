text="ABAABBC"

def get_count(w):

    return text.count(w)

most_frequent_character=max(text,key=get_count)

print(most_frequent_character)

least_recursive_character=min(text,key=get_count)

print(least_recursive_character)




