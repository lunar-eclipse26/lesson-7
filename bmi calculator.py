height = float(input("enter your height in cm: "))
weight = float(input("enter your weight in kg: "))
bmi = weight / (height/100)**2
print("your bmi is", bmi)
if bmi <= 29.3:
    print("you are underweight")
elif bmi <= 45.6:
    print("you are healthy")
elif bmi <= 55.8:
    print("you are overweight")
elif bmi <= 62:
    print("you are severly overweight")
elif bmi <= 77.7:
    print("you are obese")
else:
    print("you are very obese")