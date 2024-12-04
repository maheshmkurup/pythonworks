employee={"eid":1,"name":"Rakesh","Salary":30000,"Department":"Accounts","experience":5}

print(employee) 

employee["contact"]=3456789

print(employee) 


#if experience>5 add 10000 to current salary else add 5000

if employee["experience"]>5:

    employee["Salary"]+=10000

else:

    employee["Salary"]+=5000

print(employee)

if employee["experience"]>5:

    employee["role"]="SDE"

else:

    employee["role"]="JDE"

print(employee) 