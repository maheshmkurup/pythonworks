f1path="C:\\Users\\mahes\\OneDrive\\Desktop\\pythonworks\\file_operations_questions\\dataset2\\lines.txt"

f2path="C:\\Users\\mahes\\OneDrive\\Desktop\\pythonworks\\file_operations_questions\\dataset2\\copied_content.txt"

f_read=open(f1path,"r")

f_write=open(f2path,"w")

content=f_read.read()

f_write.write(content)

    

