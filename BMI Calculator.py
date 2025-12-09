#BMI Calculator

height = float(input("How much tall are you in meters?\n"))
weight = float(input("How much is your weight in kilograms?\n"))

BMI_formula = round(float(weight/((height/100)**2)), 2)

print ("According to the given data, your BMI is ", BMI_formula)