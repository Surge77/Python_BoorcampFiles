"""
FIFO

Implement a basic Queue data structure using
python and should have queue, dequeue and
display operations.
"""

class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items== 0

    def enqueue(self,data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return f"Dequeued element is {self.items.pop(0)}"
        else:
            print("The queue is empty")
            return None

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("The queue is empty")

    def display(self):
        if not self.is_empty():
            print("The elements of queue are: ")
            for element in reversed(self.items):
                print(element)
        else:
            print("Queue is empty")

q = Queue()

q.enqueue(3)
q.enqueue(5)
q.enqueue(9)
q.enqueue(7)
q.enqueue(1)

q.display()

print(q.dequeue())

q.display()

print(q.is_empty())



