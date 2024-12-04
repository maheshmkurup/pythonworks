weight_in_kg=int(input("Enter the weight in kg:"))

height_in_cm=int(input("Enter the height in cm:"))

height_in_meter=height_in_cm/100

BMI=weight_in_kg/(height_in_meter)**2

BMI=round(BMI,1)

print(BMI)

if BMI<19:

    print("Under Weight")

elif BMI<25:

    print("Normal Weight")

elif BMI<30:

    print("Overweight")

elif BMI>=30:

    print("obese")
