"""
WAP that has dictionary of names of students and a list of their marks in 4 subjects.Create another dictionary from this
dictionary that has name of the students and their total marks.Find out topper and his/her score.

"""

Marks = {'Neha': [97,89,94,90], 'Mitul': [92,91,94,87], 'Shefall': [67,98,34,98]}

tot = 0
tot_marks = Marks.copy()

for key,val in Marks.items():
    tot = sum(val)
    tot_marks[key] = tot
print(tot_marks)

max = 0
Topper = ''
for key,val in tot_marks.items():
    if val>max:
        max = val
        Topper = key

print(f"Topper is {Topper}, with marks {max} ")