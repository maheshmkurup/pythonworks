#list comprehension

#reference=[return loop condition]




arr=[2,3,4,5,6,7]

squares=[num**2 for num in arr]

print(squares)


cubes=[num**3 for num in arr]

print(cubes)


add_sum=[num+5 for num in arr]

print(add_sum)


even_numbers=[num for num in arr if num%2==0]

print(even_numbers)


odd_numbers=[num for num in arr if num%2!=0]

print(odd_numbers)


num_gt_five=[num for num in arr if num>5]

print(num_gt_five)
 
  