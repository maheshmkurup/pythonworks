def second_largest_number(*args):

    sorted_numbers=sorted(args,reverse=True)

    return sorted_numbers[1]

print(second_largest_number(17,12,20,6,45))

print(second_largest_number(70,24,36,17,10,67))

 

 

