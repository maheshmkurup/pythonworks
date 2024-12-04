from re import finditer

f=open("C:\\Users\\mahes\\OneDrive\\Desktop\\pythonworks\\regular_expression_fileworks\\social_posts.txt")

for line in f:

    words=line.rstrip("\n")

    pattern="#\w+"

    matcher=finditer(pattern,words)

    for obj in matcher:

        print(obj.group())