'''
ну і традиційно -> калькулятор :) повинна бути 1 ф-ція яка б 
приймала 3 аргументи - один з яких операція яку зробити!
'''



"""function wich asking try again if something wrong"""
def repeatfunc(): 
    answer = ''
    while (answer == ''):
            print("You entered something wrong!")
            answer = input('Try again? (y/n): ')
            if (answer == 'y'):
                return True
                              
            else:
                print ('Goodbye')
                return False
                break
"""calculator"""
def calc(x,o,y):
    """try is numbers are really numbers and convert them into float"""
    try:
        x = float(x)
    except ValueError:
        if(repeatfunc()):
            return True
        else: 
            return False
    try:
        y = float(y)
    except ValueError:
        """check if repeat function returns True--try again from main rogram
         False-- returns to the main program and finish"""
        if(repeatfunc()):
            return True
        else: 
            return False
        """check what operator was given"""
    if (o =='+'): return print(x + y)
    elif (o =='-'): return print(x - y)
    elif (o =='*'): return print(x * y)
    elif (o =='/'):
        try:
            return print(x / y)
        except ZeroDivisionError:
            print("You can't divide by 0!")
            if(repeatfunc()):
                return True
            else: 
                return False
        
    else : 
        if(repeatfunc()):
            return True
        else:
            return False
        
while True:
    """input values and cutting off all whitespaces"""
    x = input("first number:").replace(" ", "")
    o = input("operator:").replace(" ", "")
    y = input("second number:").replace(" ", "")

    print(x,o,y,end=" = ")
    """if calculator func return false finish the program else try from the begining"""
    if (calc(x, o, y) == False):
        break
    else: 
        continue 
"""Я не уверен правильно ли пользоваться while true, возможно это занимает 
много памяти"""       