"""
Find the word in the string and if present print
the word in all capital letters else print Not
present.
"""


def find_word(word,sentence):
    words = sentence.split()
    if word in words:
        index = words.index(word)
        # words[index] =  word.upper()
        # sentence = ''.join(words)
        print(f'The word "{word}" is present in the sentence at index {index} and in Uppercase: {word.upper()}')
    else:
        print(f"The word {word} not present in the sentence")

sentence = 'Python is a popular programming language for web and mobile development.'
word = 'programming'

find_word(word, sentence)