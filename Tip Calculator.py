#Tip calculator

print ("Welcome to the Tip Calculator")

total_bill = float ( input ("How much is the bill?\n"))
members = int (input ("How many members are there?\n"))

question = input("Do you want to split the bill or first tip then split the bill?\n")

if question == "split":
    print (f"According to the information, each will have to give  {round(total_bill/members, 2)}")
elif question == "tip":
   tip = int( input ("How much percent Tip you want to give? 10, 12, 15 or 20?\n"))
   each_give = ((total_bill) + (total_bill*(tip/100))) / members
   print (f"According to the information, each will have to give {round (each_give, 2)}")
