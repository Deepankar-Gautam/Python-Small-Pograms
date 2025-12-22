# sum of even numbers

total_number = 0

    #   method 1

for i in range (1, 101):
    if i % 2 == 0:
        total_number += i
print (total_number)
total_number = 0        # to reset the value for method 2
    #   method 2 

for i in range (2, 101, 2):
    total_number += i
print (total_number)

# same for odd values, just need to change the digits and some conditions