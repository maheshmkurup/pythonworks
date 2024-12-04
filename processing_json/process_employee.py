from json import load

f=open("C:\\Users\\mahes\\OneDrive\\Desktop\\pythonworks\\datasets\\employee.json")

data=load(f)

for emp in data:

    print(emp)

    