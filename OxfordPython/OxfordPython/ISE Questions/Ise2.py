"""

Outputs the sum of the digits in the string after splitting them up
"""


st ="Amit:9262,Jon:6125"
x = st.split(",")
print(st)
#print(x)
y1 = x[0].split(":")
y2 = x[1].split(":")
#print(y1)
#print(y2)
y12 = list(y1[1])
y22 = list(y2[1])
#print(y12)
#print(y22)
print(y1[0],"=",int(y12[0])+int(y12[1])+int(y12[2])+int(y12[3]))
print(y2[0],"=",int(y22[0])+int(y22[1])+int(y22[2])+int(y22[3]))