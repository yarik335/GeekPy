'''
Створіть 3 різних функції(на ваш вибір), кожна з цих функцій повинна повертати 
якийсь результат. Також створіть четверу ф-цію, яка в тілі викликає 3 
попередніб обробляє повернутий ними результат та також повертає результат. 
Таким чином ми будемо викликати 1 функцію, а вона в своєму тілі ще 3
'''
def func1(n, x = 0, y = 0): #correcting x and y in loop
    
    for i in range(0,n): 
        x = x + 0.1
        y = y - 0.1
    return (x,y)
    
def func2(a = "hello ", b = "new Legioner!"): #return string username + id or defaults
    if(not(a == 'hello ' and b == 'new Legioner')):
        c ="username: " + a + " userId: " + b
    return c

def func3(s,c,p): #just some simple calculating
    
    return str(s+c/p)

def func4(info = {},*args,**kwargs): #join functions before and add args + kwargs

    if(info == {}):    
        func1(5)
        func2()
        func3(1, 220, 3.14)
    else: 
        print(info) 
    s = str(func1(args[0])) + func2(args[1],args[2]) + func3(kwargs['sprint'], kwargs['charley'], kwargs['Pi'])
    return s
print(func4({},2,"yarik","335 ",sprint=5,charley=8,Pi=3.14))

