f=open("C:\\Users\\mahes\\OneDrive\\Desktop\\pythonworks\\file_operations_questions\\dataset2\\word_occurences.txt")

search_element="program"

for line in f:

    words=line.split(" ")

    words.count(search_element)

print(search_element)