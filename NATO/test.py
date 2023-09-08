student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    pass

#Loop through data frame:

import pandas 

student_data_frame = pandas.DataFrame(student_dict)

#Loop through a data frame.

for (key, value) in student_data_frame.items():
    pass
#Loop through row of a data frame.
for (index, row) in student_data_frame.iterrows():
    pass

# #TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

new_dict = {row.student: row.score for (index, row) in student_data_frame.iterrows()}
print(new_dict)


# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

