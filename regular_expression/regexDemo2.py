from re import finditer

text="I have 3 cars,2 bike and 1 Cycle"

#pattern="[a-zA-Z]"#==>"[a-z]" checks for only low case alphabets and"[a-zA-Z]" checks for all alphabets

#pattern="[0-9]"#=> check for digits

#pattern="[a-zA-Z0-9]"#=> check for both alphabets and numbers (alphanumeric) or "\w"

#pattern="[^ak]"#=> exclude a and k

#pattern="[^akA-Z0-9 ]" #=> exclude a and k and print all lower case characters

pattern="[^a-zA-Z0-9]" #=> print special characters

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())





    







