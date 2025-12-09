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

# average height of students

# heights = input ("Tell me all the heights with ', ' and I will tell you the average height of the students!\n").split (", ")

# total_height = 0
# members = 0

# for i in range (len(heights)):
#     heights[i] = int(heights[i])

# for height in heights:
#     total_height += height
# print (total_height)

# for height in heights:
#     members = members + 1
# print (members)

# average = total_height/members

# print (f"So the average height of the class is {round(average)}")

###################################################################

# finding the average height of the students

# height = input ("Tell me all the height of the sutdents : ").split(", ")

# total_height = 0
# total_students = 0

# for i in range (len(height)):
#     height[i] = int(height[i])

# for individual_sum in height:
#     total_height += individual_sum

# for number in height:
#     total_students += 1

# average = total_height / total_students

# if average.is_integer():
#     print (int(average))
# else:
#     print (f"{average : .2f}")


#############################################################


# max and min score of the class

# scores = input ("Tell me all the score of the class : ").split(", ")

# high_score = 0
# low_score = 0 
# for i in range (len(scores)):
#     scores[i] = int (scores [i])

# for maxu in scores:
#     if maxu > high_score:
#         high_score = maxu
# print (f"The highest score of the class is : {high_score}")
# for minu in scores:
#     if minu < low_score:
#         low_score = minu
# print (f"The lowest score of the class is : {low_score}")

# # another method with sorting 

# for maxu in scores:
#     scores.sort()
# print (f"The highest score of the class is : {scores[-1]}")
# print (f"The lowest score of the class is : {scores[0]}")

############################################

# printing 1 to 100
# total_num = 0
# for i in range (1, 101):
#     total_num += i
# print (total_num)

############################################

# printing even numbers

# total_number = 0

#       method 1

# for i in range (1, 101):
#     if i % 2 == 0:
#         total_number += i
# print (total_number)

#       method 2 

# for i in range (0, 101, 2):
#     total_number += i
# print (total_number)

############################################


n = 1

while True:
    print(n ** 998)
    n += 1































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