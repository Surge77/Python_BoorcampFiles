"""
WAP that forms a list of first character of every word in another list
"""

List1 = ["Hello","Welcome","to","the","world","of","python"]

letters = []
for word in List1:
    letters.append(word[0])

print(letters)
