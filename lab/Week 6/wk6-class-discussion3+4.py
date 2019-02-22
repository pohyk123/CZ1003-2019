#Data structure for storing score for each student, belonging to a tutorial/lab group
import random as r

#Dictionary of ID (lab_group, id): score
grades = {
    ('SS1', 1) : r.randint(1,100),
    ('SS1', 2) : r.randint(1,100),
    ('SS1', 3) : r.randint(1,100),
    ('SS1', 4) : r.randint(1,100),
    
    ('SS2', 1) : r.randint(1,100),
    ('SS2', 2) : r.randint(1,100),
    ('SS2', 3) : r.randint(1,100),
    ('SS2', 4) : r.randint(1,100),
}

print(grades)
print("('SS1',1) :",grades[('SS1',1)])

#List comprehension to extract score element from tuple
class_ss1_scores = [x[1] for x in grades if 'SS1' in x]
class_ss2_scores = [x[1] for x in grades if 'SS2' in x]

#Find avg & max scores in class 1/2
avg_classSS1 = sum(class_ss1_scores)/len(class_ss1_scores)
avg_classSS2 = sum(class_ss2_scores)/len(class_ss2_scores)
max_class_SS1 = max(class_ss1_scores)
max_class_SS2 = max(class_ss2_scores)

#Compare avg & max values between class 1 & 2
if(avg_classSS1 > avg_classSS2):
    print('Class 1 has higher average score.')
else:
    print('Class 2 has higher average score.')
    
if(max_class_SS1 > max_class_SS2):
    print('Class 1 has higher max score.')
else:
    print('Class 2 has higher max score.')