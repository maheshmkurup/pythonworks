#class => design or template or blueprint

#object => created with the help of class


#class str:

    #attributes
    #methods 

#To create object
#reference_name=className()


#capitalize()=> make the first letter capital
#casefold()=> make capital letters into small letters
#isalpha()=>return true if all are alphabets
#isdigit()=>return true if all are digits
#isalnum()=>return true if it contains both alphabets and digits
#startswith(str)=>returns true if it is the starting of specified string
#endswith(str)=>returns true if it is the stopping of specified string

#text="HellPython12"

#print(text.capitalize())

#print(text.casefold()) 

#print(text.isalpha())

#print(text.isdigit())

#print(text.isalnum()

#print(text.startswith("He"))

#print(text.endswith("12"))


#for ch in text:

    #print(ch)


#text="hello,world,python"

#words=text.split(",")

#print(words)

#lstrip=>remove left

#rstrip=>remove right 

#text="\t this is \ta line\t"

#new_text=text.strip("\t")

#print(new_text)


#replace

#text="hello world program"

#replace a=>o

#new_text=text.replace("o","a")

#print(new_text)

#Slicing

text="python programming"

      #012345678901234567 => index values
      #string_object[start:end:step] => Syntax

print(text[:6])

print(text[7:])

print(text[::2])

print(text[::-1])  #reversing a string
