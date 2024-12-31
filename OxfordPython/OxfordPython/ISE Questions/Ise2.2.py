"""

So, overall, the code takes the string, splits it into individual name-number pairs, processes each pair to find the
product of the smallest and largest digits in the number, and then prints out the result along with the associated name.

"""


st ="Amit:6587,Jon:3289"
x = st.split(",")
print(st)
#print(x)
y1 = x[0].split(":")
y2 = x[1].split(":")
print(y1)
print(y2)
y12 = list(y1[1])
y22 = list(y2[1])
print(y12)
print(y22)
y12.sort()
print(y12)
y22.sort()
print(y22)
r1 = int(y12[0]) * int(y12[-1])
r2 = int(y22[0]) * int(y22[-1])
print(y1[0],"=",r1)
print(y2[0],"=",r2)