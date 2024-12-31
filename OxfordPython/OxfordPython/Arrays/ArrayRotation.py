"""
Python Program for array rotation

"""

import array


def rotate(arr,num_positions):
    for i in range(num_positions):
        arr.append(arr.pop(0))




arr = array.array('i',[1,2,3,56,12,43,89,65,78,98,4,5,6])


pos = int(input("Enter the number of positions to rotate: "))

print(f"original array is: {arr}")
rotate(arr,pos)

print(f"New array {arr}")

