st1={1,2,3}

st2={1,2,3,4,5}

print(st1.issubset(st2))


print(st2.issuperset(st1))


symmetric_difference=st1.symmetric_difference(st2)

print(symmetric_difference)  #=>AUB-A^B


st1.update(st2)

print(st1)


text="this is a test to remove duplicate words this test is simple"

text2="this simple test remove duplicate words"

words=text.split(" ")

print(set(words))

print(set(text2).issubset(text))

 


