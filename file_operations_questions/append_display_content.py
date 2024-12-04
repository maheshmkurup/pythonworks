f=open("C:\\Users\\mahes\\OneDrive\\Desktop\\pythonworks\\file_operations_questions\\dataset2\\subjects.txt","a")

subject1=input("Enter the subject1 to append:")

subject2=input("Enter subject2 to append:")

for sub in subject1,subject2:

    f.write(sub+"\n")

f.close()

