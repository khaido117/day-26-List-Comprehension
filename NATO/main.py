import pandas 

#Read the file
nato_data = pandas.read_csv("/Users/khaido/Library/CloudStorage/GoogleDrive-khaitroyy@gmail.com/My Drive/Code/day-26-List-Comprehension/NATO/nato_phonetic_alphabet.csv")

#Convert to dictionary
data_dict = nato_data.to_dict()

nato_data_frame = pandas.DataFrame(data_dict)
# print(nato_data_frame)

##TODO 1. Create a dictionary to this format.
nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

#TODO 2:

word = input("Enter your name: ").upper()

##Option 1
# for letter in word:
#     list = []
#     list.append(nato_dict[letter])
#     print(list)

##Option 2 - shorten code
name_spelling = [nato_dict[letter] for letter in word]
print(name_spelling)



