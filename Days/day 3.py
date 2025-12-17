


##################################################################

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
    
#####################################################################

# story, a stupid story making prject

print ("Welcome to the Treasure Island")
print ("Your mission is to find the treasure")

lr = input ("""You were on a treasure hunt. During the hunt you reach a T point.
What will you choose, left or right? \n""")

if lr.lower() == "right":
    print ("Game over, you fell in the hole.")

sw = input ("""You moved to left, walked 3km and reach at the bank of the river,
will you swin or wait for the boat?\n""")

if sw.lower() == "swim":
    print ("Game over, you got eaten by crocodiles")

door = input ("""You crossed the river, walked 5km and found a cave. 
You entered there and found that there are 3 doors, Red, Blue and Yellow, which will you choose?\n""")

if door.lower() == "blue" or door.lower() == "red":
    print ("Game over, you got eaten by monsters")
else:
    print ("You found the treasure, you won the game")

####################################################################################

# stupid love calcualtor

yname = input ("So what is your name?\n").lower()
tname = input ("And their name?\n").lower()

count_t = (yname.count("t") + tname.count("t"))
count_r = (yname.count("r") + tname.count("r"))
count_u = (yname.count("u") + tname.count("u"))
count_e = (yname.count("e") + tname.count("e"))
count_l = (yname.count("l") + tname.count("l"))
count_o = (yname.count("o") + tname.count("o"))
count_v = (yname.count("v") + tname.count("v"))
count_e2 = (yname.count("e") + tname.count("e"))

tens = (count_t + count_r + count_u + count_e)*10
ones = count_l + count_o + count_v + count_e2

percent = tens + ones

if percent > 90 or percent < 10:
    print (f"Your compatibility percent is {percent}%, you go together like coke and mentos")
elif percent > 50 or percent < 40:
    print (f"Your compatibility percent is {percent}%, you are alright together")
