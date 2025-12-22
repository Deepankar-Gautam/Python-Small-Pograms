# PIZZA Order

print ("Welcome to Nigga Dominos\n")
print("""---Nigga Menu---
Small pizza : 15$
Medium pizza : 20$
Large pizza : 25$""")
bill = 0
size = input ("What size do you want, S M or L: ")

if size.lower() == "s":
    bill += 15
    print (f"Your current bill: {bill}$")

elif size.lower() == "m":
    bill += 20
    print (f"Your current bill: {bill}$")
elif size.lower() == "l":
    bill += 25
    print (f"Your current bill: {bill}$")

add = input("Do you want to add something? Y or N: ")

if add.lower() == "y":
    if size == "s":
        pepperoni = input("Add pepperoni for 2$: Y or N: ")
        if pepperoni.lower() == "y":
            bill += 2
            print (f"Your current bill: {bill}$")
    elif size == "m":  
        pepperoni = input("Add pepperoni for 3$: Y or N: ")
        if pepperoni.lower() == "y":
            bill += 3
            print (f"Your current bill: {bill}$")
    elif size == "l":
        pepperoni = input("Add pepperoni for 5$: Y or N: ")
        if pepperoni.lower() == "y":
            bill += 5
            print (f"Your current bill: {bill}$")
else:
    print("Invalid answer")

xcheeze = input ("Add extra cheese for 1$: Y or N: ")
if xcheeze.lower() == "y":
    bill += 1
    
print (f"Your total bill: {bill}$")
    