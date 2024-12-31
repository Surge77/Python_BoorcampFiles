
import array

vals = array.array('i',[23,2,1,6,6])

vals.reverse()
vals.append(3)
vals.remove(6)


print(vals)