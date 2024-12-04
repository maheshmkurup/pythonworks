f=open("C:\\Users\\mahes\\OneDrive\\Desktop\\pythonworks\\datasets\\fruits.txt","r")

fruits=[]

for line in f:

    fruits.append(line.rstrip("\n"))

print(fruits)

  