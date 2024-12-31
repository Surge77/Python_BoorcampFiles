"""
Write a python program to count the numbers
appearing in the list and print the count
"""

def count_number(nums,n):
    count = 0
    for num in nums:
        if num==n:
            count += 1

    return count

numbers = [2, 3, 5, 2, 11, 2, 7]

number_to_count = 2

print(f"Count of {number_to_count} in the list is : {count_number(numbers,number_to_count)}")
