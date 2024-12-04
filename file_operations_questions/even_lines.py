f=open("C:\\Users\\mahes\\OneDrive\\Desktop\\pythonworks\\file_operations_questions\\dataset2\\lines.txt")

for index,line in enumerate(f,start=1):

    if index%2==0:

        print(line.strip())