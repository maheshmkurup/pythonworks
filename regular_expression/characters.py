from re import finditer

text="I have 3 cars,2 bike and 1-Cycle"

#pattern="\w" #=>"[a-zA-Z0-9]" alphanumeric

#pattern="\d" #=>"[0-9]" digits

#pattern="\D"  #=>"[^0-9]" exclude digits

#pattern="\W" #=>"[^a-zA-Z0-9]" Special characters

#pattern="\s" #=> white spaces 

pattern="\S"  #=> exclude spaces

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())



