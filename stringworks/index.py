#text="hello world"

#print(text.index("o"))


#text="vipinkumar@gmail.com"

#at_index=text.index('@')

#print(text[0:at_index])

text="hellopython"

index_o=text.index("o")

reversed_substring=text[index_o-1::-1]

balance_substring=text[index_o:]

result=reversed_substring+balance_substring

print(result)

 