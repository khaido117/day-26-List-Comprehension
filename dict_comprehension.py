import random 
import pandas

names = ["Alex", "Beth", "Caroline", "Dave", "Aleanor", "Freddie"]
student_score = {student:random.randint(1,100) for student in names}

passes_student = {student:score for (student, score) in student_score.items() if score >= 60}


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dicitonaries.
# for (key, value) in student_dict.items():

student_data_frame = pandas.DataFrame(student_dict)

#Loop through a data frame.

for (key, value) in student_data_frame.items():
    print(key, value)

#Loop through rows of a data frame.
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
      print(row.score)

