"""
WAP to show implementation of a queue using list data structure
"""

queue = [1,2,3,4,5,6]

print("Original queue is : ",queue)

queue.append(7)
print("queue after insertion: ",queue)

queue.pop(0)

print("Stack after deletion : ",queue)

last_element_index = len(queue) - 1
print("Value obtained after peep operation is : ",queue[last_element_index])