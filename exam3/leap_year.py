year=int(input("Enter the year:"))

if (year%100!=0 and year%4==0) or (year%100==0 and year%400==0):

    print(f"{year} is a leap year")

else:

    print(f"{year} is not leap year")
