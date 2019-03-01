#Build a database of scores and various functions for reading/writing it.

grades = {}

#Inserts a new record
def inputRecord(dataBase,group,id,score):
    dataKey = (group,id)
    dataBase[dataKey] = score
    
#Query an entry based on group # and ID
def query(dataBase,group,id):
    try:
        key = (group,id)
        return dataBase[key]
    except:
        return None
        
#returns scores for all members of a chosen group
def listGrades(dataBase,group):
    listOfScores = []
    for key,score in dataBase.items():
        grp,id = key
        if(grp==group):
            listOfScores.append(score)
    return listOfScores
    
#Returns the highest score
def maxGrade(dataBase,group):
    listOfScores = listGrades(dataBase,group)
    return max(listOfScores)

#Insert dummy records
inputRecord(grades,1,1,80)
inputRecord(grades,1,2,70)
inputRecord(grades,2,3,60)

#query a record's score value
score = query(grades,1,2)
print(score)

#list grades from chosen group & display max score
group1Grades = listGrades(grades,1)
group1MaxGrade = maxGrade(grades,1)
print(group1Grades,group1MaxGrade)