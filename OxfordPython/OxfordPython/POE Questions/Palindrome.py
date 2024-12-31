
"""
Write a program in Python to check if a sequence is a Palindrome. (Use sequence 1234321 )
"""

def is_palindrome(sequence):
    return sequence == sequence[::-1]

sequence = '1234321'

if is_palindrome(sequence):
    print(f'The sequence {sequence} is a palindrome')
else:
    print(f'The sequence {sequence} is not a palindrome')