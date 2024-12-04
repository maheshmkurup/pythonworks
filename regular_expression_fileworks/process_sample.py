from re import findall

f=open("C:\\Users\\mahes\\OneDrive\\Desktop\\pythonworks\\regular_expression_fileworks\\sample.txt")

content=f.read()

pattern="https?://[\ w\S./]+"

urls=findall(pattern,content)

for url in urls:

    print(url)

