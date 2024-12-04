from re import finditer

text="abbbababbabaaaab"
     #0123456789012345

#pattern="a{2}" #=> check for 2a's in the text    

pattern="a{1,3}"

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())

