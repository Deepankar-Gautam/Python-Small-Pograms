# for i in range (1, 11):
#     if i % 2 == 0:
#         print ("meow")
#     else:
#         print (i)

# for i in range (1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print ("FizzBuzz") 
#     elif i % 3 == 0:
#         print ("Fizz")
#     elif i % 5 == 0:
#         print ("Buzz")

###########################################################

# printing 1 to 100
# total_num = 0
# for i in range (1, 101):
#     total_num += i
# print (total_num)

############################################



############################################


# n = 1

# while True:
#     print(n ** 998)
#     n += 1































# printing every 3rd number under 100

# for i in range (1, 100, 3):
#     print (i)

# printing table of 3

# for i in range (0, 11):
#     if i == 0:
#         continue
#     print (f"3 X {i} = {i*3}")

# reverse a fucking string

# string = input ("Give me your string: ")

# new_string = ""

# for characters in string:
#     new_string = characters + new_string #ch + new_string is important

# print (new_string)



user = input ('Is it a palindrome? \n')

for i in user:
    if i == -1:
        print ("Yes it's  a palindrome")