def func1(f,*args,c=None):
    total = 0
    for i in args:
        total = total + i
    return total

res = func1(2,3,4,5,6,7,8,9,0,23,4,5,6,6,50,2)

print(res)
