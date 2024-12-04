weight_in_kg=int(input("Enter the weight in kg:"))

height_in_cm=int(input("enter the weigh in cm:"))

height_in_meter=height_in_cm/100

bmi=weight_in_kg/height_in_meter**2

bmi=round(bmi,1)

print(bmi)