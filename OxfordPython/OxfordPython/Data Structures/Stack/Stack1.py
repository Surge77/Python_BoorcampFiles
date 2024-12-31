"""


Push/Pop element : O(1)
Search element by value: O(n)

LIFO


"""


class Stack:

    def __init__(self):
        # this list will be used to store the elements of the stack
        self.items = [] # initializes a new empty list items, which will be used to store the elements of the stack.

    def is_empty(self):
        return len(self.items) == 0  # here equality operator is used as it will return true or false whether list is empty or not

    def push(self,data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return f"The popped element is {self.items.pop()}"  # This method removes and returns the top item from the stack. Since it removes an item and needs to return it, it includes a return statement to return the popped item to the caller.
        else:
            print("The list is empty")
            return None

    def size(self):
        return len(self.items)

    def peek(self): # return the top item from the stack without removing it.
        if not self.is_empty():
            return self.items[-1] # this is negative indexing which returns the last item or latest element added in stack
        else:
            print("The list is empty")

    def display(self):
        if not self.is_empty():
            print("Stack elements:")
            for item in reversed(self.items):
                print(item)
        else:
            print("Stack is empty")

o = Stack()

o.push(34)
o.push(44)
o.push(4)

o.display()

print(o.pop())
print(o.pop())
o.push(6)

o.display()

print(o.pop())

print(o.peek())
print(o.size())

print(o.is_empty())

