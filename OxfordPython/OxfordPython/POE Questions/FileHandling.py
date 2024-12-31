"""
Write a python program to create a file named
“my_file.txt” and write three lines inside it.
"""

# Open the file in write mode ('w') and assign the file object to a variable (file_obj).
with open('my_file.txt', 'w') as file_obj:
  # Write three lines to the file using the write() method.
  file_obj.write('Hello, world!\n')
  file_obj.write('This is the second line.\n')
  file_obj.write('This is the third line.\n')

  # Close the file using the close() method.
  file_obj.close()

  # Note that if you forget to close the file, it may remain open and consume system resources.
  # In addition, any changes made to the file may not be saved to disk until the file is closed.

  # In this program, we use the open() function to open a file named "my_file.txt" in write mode ('w').
  # We then use a with statement to ensure that the file is properly closed after we are done writing to it.

  # After the with block, the file is automatically closed and the changes are saved to disk.

  # Note that if the file "my_file.txt" already exists, this program will overwrite it. If you want to append to an
  # existing file instead of overwriting it, you can open the file in append mode ('a') instead of write mode ('w').