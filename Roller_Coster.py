# Rollercoster example

print ("Welcome to the Rollercoster Ride")
height = float( input ("How much tall are you?\n"))
ticket = 0

if height >= 120:
    print ("You can ride the Rollercoster")
    age = int( input ("What is your age?\n"))
    if age < 12:
        ticket += 7
        print (f"You have to pay {ticket}$\n")
    elif age < 18:
        ticket += 10
        print (f"You have to pay {ticket}$\n")
    elif age >= 45 and age <= 55:
        ticket = 0
        print (f"Due to mid life crisis, you have to pay {ticket}$\n")
    else:
        ticket += 12
        print (f"You have to pay {ticket}$\n")
        print 

    photo = input ("If you want a photo which cost's 3$, say 'yes'\n")
    if photo.lower() == "yes":
        ticket += 3
        print (f"Then your total bill is {ticket}$")
    else:
        print (f"Then your total bill is {ticket}$")

else:
    print ("You are not eligible to ride on the Rollercoster")