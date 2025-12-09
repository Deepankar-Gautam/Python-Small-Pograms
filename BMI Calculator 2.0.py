# BMI Calculator 2.0

height = float (input ("How much tall are you in cm?\n"))
weight = float (input ("How much is your weight in kilograms?\n"))

BMI = round( float(weight / (height/100) ** 2), 2)

if BMI <= 18.5:
    print (f"Your BMI is {BMI}, are underweight")
elif BMI <= 25:
    print (f"Your BMI is {BMI}, weight is normal")
elif BMI <=30: 
    print (f"Your BMI is {BMI}, are overweight")
elif BMI <= 35:
    print (f"Your BMI is {BMI}, are obese")
else:
    print (f"Your BMI is {BMI}, are clinically obese")
