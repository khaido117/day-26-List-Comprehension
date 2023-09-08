#List comprehension example 1.
numbers = [1,2,3]

new_numbers = [num + 1 for num in numbers]

#Example 2 with string.
name = "Angele"
new_list = [letter for letter in name]

#Example 3 with range.
new_range = [num * 2 for num in range(1,5)]

#Example 4 with conditional.

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor","Freddie"]

short_names = [name for name in names if len(name) < 5]
cap_names = [name.upper() for name in names if len(name) >= 5 ]
print(cap_names)

