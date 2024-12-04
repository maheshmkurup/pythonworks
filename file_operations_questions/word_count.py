f=open("C:\\Users\\mahes\\OneDrive\\Desktop\\pythonworks\\file_operations_questions\\dataset2\\wordtextfile1.txt","r")

words=[]

for line in f:

    line=line.rstrip("\n")

    all_words=line.split(" ")

    for w in all_words:

        words.append(w)

word_count={w:words.count(w) for w in words}

print(word_count)








