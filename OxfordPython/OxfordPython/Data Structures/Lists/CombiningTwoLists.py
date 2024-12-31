"""
WAP that creates a list of words by combining the words in two individual lists
"""

list_words = []

for x in ["Hello","World"]:
    for y in ["Python","programming"]:
        word = x+y
        list_words.append(word)

print("The list after combining two individual list is :",list_words)