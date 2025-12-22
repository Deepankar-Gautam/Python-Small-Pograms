# finding the average height of the students
# can't use sum() and len()

height = input ("Tell me all the height of the sutdents : ").split(",")

total_height = 0
total_students = 0

for i in range (len(height)):
    height[i] = int(height[i].strip())

for individual_sum in height:
    total_height += individual_sum

for number in height:
    total_students += 1

average = total_height / total_students

if average.is_integer():
    print (int(average))
else:
    print (f"{average : .2f}")