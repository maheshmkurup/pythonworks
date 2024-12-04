#lambda functions

#lambda function for adding two numbers

sum=lambda n1,n2:n1+n2

print(sum(100,200))


#lamba function for subtracting two numbers

difference=lambda n1,n2:n1-n2

print(difference(15,2))



#lamba function for finding the cube of a number

cube=lambda n:n**3

print(cube(3))


#lambda function for finding maximum of two strings

max_two=lambda str1,str2: str1 if len(str1)>len(str2) else str2

print(max_two("Hai","Hello"))


#lambda function for finding minimumof two strings

min_two=lambda str1,str2: str1 if len(str1)<len(str2) else str2

print(min_two("hai","hello"))


#lambda function for finding smart_sub

smart_sub=lambda n1,n2: n1-n2 if n1>n2 else n2-n1

print(smart_sub(20,50))


words=["hello","hai","morning","test","apple"]

def get_length(word):

    return len(word)

print(max(words,key=get_length))


#using lambda function 

gett_length=lambda word:len(word)

print(max(words,key=gett_length))

 

