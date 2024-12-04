f=open("C:\\Users\\mahes\\OneDrive\\Desktop\\pythonworks\\file_operations_questions\\dataset2\\word_occurences.txt","r")

character_frequency={}

for lines in f:

 for ch in lines:

    if ch in character_frequency:

        character_frequency[ch]+=1

    else:

        character_frequency[ch]=1

print(character_frequency)
