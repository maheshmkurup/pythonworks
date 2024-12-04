text="on june 5th,2024,we will celebrate @ our annual event: 'Tech innovations 2024!"

alphabets_count=sum(c.isalpha() for c in text)

space_count=text.count('')

number_count=sum(c.isdigit() for c in text)

special_character_count=sum(not c.isalnum() and not c.isspace() for c in text)

print(f"alphabtes={alphabets_count}")

print(f"numbers={number_count}")

print(f"spaces={space_count}")

print(f"special_character={special_character_count}")