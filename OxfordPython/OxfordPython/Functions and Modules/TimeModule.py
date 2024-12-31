"""
WAP to display the date and time using the time module
"""

import time

localtime = time.asctime(time.localtime(time.time()) )
print("Local current time : ",localtime)