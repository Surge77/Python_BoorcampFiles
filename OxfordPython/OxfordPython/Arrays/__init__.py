def rotate_array(arr, n):
    """
    Function to rotate an array by 'n' positions to the right.

    Parameters:
    arr (list): The input array.
    n (int): The number of positions to rotate the array.

    Returns:
    list: The rotated array.
    """
    # Calculate the length of the array
    length = len(arr)

    # Handle cases where 'n' is greater than the length of the array
    n = n % length

    # Slice the array and concatenate the rotated parts
    rotated_arr = arr[length - n:] + arr[:length - n]

    return rotated_arr


# Example usage:
arr = [1, 2, 3, 4, 5]
n = 2
print("Original array:", arr)
print("Array after rotating by", n, "positions:", rotate_array(arr, n))
