"""
WAP that prompts the user to enter a message.Now count and print the number of occurrences of each character

Dict.get(key) : returns teh value for the key passed as argument.If the key is not present in dictionary it will return
the default value.If no default value is specified then it will return None

"""


def count(message):
    letters_count = {}
    for letter in message:
        letters_count[letter] = letters_count.get(letter,0) + 1
    print(letters_count)

message = input("Enter a message: ")

count(message)

