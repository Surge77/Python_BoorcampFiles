"""
Write a python program to use split and join
methods in the given string and trace a word.
"""

def trace_word(word, sentence):
    words = sentence.split()
    for i, w in enumerate(words):
        if w == word:
            print(f'The word "{word}" is at index {i}')

sentence = 'Python is a popular programming language for web and mobile development.'
word = 'programming'

trace_word(word, sentence)