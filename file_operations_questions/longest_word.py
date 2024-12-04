f=open("C:\\Users\\mahes\\OneDrive\\Desktop\\pythonworks\\file_operations_questions\\dataset2\\longest.txt")

for line in f:

    words=line.split(" ")

    max_word=max(words,key=len)

print(max_word)