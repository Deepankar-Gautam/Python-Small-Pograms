# max and min score of the class

scores = input ("Tell me all the score of the class : ").split(",")
 
for i in range (len(scores)):
    scores[i] = int (scores [i].strip())

high_score = scores[0]
low_score = scores[0]

for maxu in scores:
    if maxu > high_score:
        high_score = maxu

for minu in scores:
    if minu < low_score:
        low_score = minu

print (f"The highest score of the class is : {high_score}")
print (f"The lowest score of the class is : {low_score}")

# another method with sorting 


scores.sort()
print (f"The highest score of the class is : {scores[-1]}")
print (f"The lowest score of the class is : {scores[0]}")