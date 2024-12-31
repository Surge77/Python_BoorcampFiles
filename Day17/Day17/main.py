# we created a class named user
# the name of class is given according to the PascalCase
# PascalCase => First letter of every word should be capitalized
# camelCase => In this casing the first word is in small letter and for every other word the first letter is capital
# snake_case => every starting letter is lower case but every word separated by an underscore
class User:

    # Constructor
    # We can pass as many parameter to set the attributes
    # It is helpful when we want to create a lot of objects with same attributes
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # To set a default value in constructor
        self.followers = 0


# indentation is required to add contents to the class
# Pass is used to signify that the class is empty

user_1 = User("001", "Mike")
user_2 = User("002", "Tejas")

print(user_2.followers)
# Object created from User() class and stored in user_1

# Creating attribute for the class
# To create it first tap into the object and add the attribute
# An attribute is a variable associated with an object
#
# user_1.id = "001"
# user_1.name = "MIke"

# print(user_1.name)

# To avoid these initialization of attributes every time we create a object we use a Constructor
# Constructor Is a special member function which is automatically invoked when an object of a class is created
# It is also known as initializing the object
