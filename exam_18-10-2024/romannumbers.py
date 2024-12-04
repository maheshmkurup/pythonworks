numbers_dictionary={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",10:"X"}

number=int(input("Enter the number:"))

if number in numbers_dictionary:

    print(numbers_dictionary.get(number))
