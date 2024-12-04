#result={key:value,iteration,condition}

#arr=[10,20,30,40,2,3,9,7,15]

#result={num:num**3 for num in arr}

#print(result)


arr=[10,20,30,40,2,3,7]

even_squares={num:num**2 for num in arr if num%2==0}

print(even_squares)

odd_cubes={num:num**3 for num in arr if num%2!=0}

print(odd_cubes)

