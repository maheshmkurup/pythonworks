text="ABBACB"

character_count={}

for ch in text:

    if ch in character_count:

        character_count[ch]+=1

    else:

        character_count[ch]=1

print(character_count)

text="ABBACB"

character_count={}

for ch in text:

    if ch in character_count:

        print(f"The First recursive character is:",ch)

        break

    else:

        character_count[ch]=1




 














