weight=int(input("Enter the weight in kg:"))

height_in_cm=int(input("Enter the height in cm:"))

height_in_meter=height_in_cm/100

BMI=weight//height_in_meter**2

print(BMI)

if BMI<19:

    print("Underweight")

elif BMI>19 and BMI <25:

    print("Normal weight")

elif BMI>25 and BMI<30:

    print("Overweight")

elif BMI>30:

    print("Obese")

