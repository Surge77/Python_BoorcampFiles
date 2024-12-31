
# Attributes are the things that the object has
# Methods are the things that the object does
# When a function is attached to an object it is called a method

# Creating methods in class

class User:

    # This is a reference to the instagram model of followers following ..etc
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # Creating a method
    # A method always has a self parameter
    # That means this method knows the object that called it
    def follow(self,user):
        user.followers += 1  # we follow other user
        self.following += 1 # self means our own



user_1 = User("001","James")
user_2 = User("002","Sydney")

user_1.follow(user_2)
# user_1 object and the follow method
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)