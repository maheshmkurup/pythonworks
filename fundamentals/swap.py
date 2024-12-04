num1=100
num2=200
print(f"num1={num1}")
print(f"num2={num2}")
# logic 1
# temp=num1
# num1=num2
# num2=temp

# logic2

num1=num1+num2    
num2=num1-num2
num1=num1-num2
print(f"After swapping num1={num1} and num2={num2}")

