# Fizz Buzz question
# print 1 to 100, if a number is divisible by 3, print "Fizz",
# if divisible by 5, print "Buzz", if divisible by both, print FizzBuzz

for i in range (1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print ("FizzBuzz")
    elif i % 5 == 0:
        print ("Buzz")
    elif i % 3 == 0:
        print ("Fizz")
    else:
        print (i)