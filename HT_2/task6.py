'''
придумайте 3 різних ф-ції(немає різниці які)
'''
def verticalmove(y):
    return y+10
def horizontalmove(x):
    return x+10

def func3(x,y,z=0):
    if(z == 0):
        t = y
        x+=y
        y+=t
        
    y = verticalmove(y)
    x = horizontalmove(x)
    return [x,y,z]
print(func3(1,1,0))