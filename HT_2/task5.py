'''
маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клаві
створюєте ф-цію яка буде отримувати рядки на зразок мого, яка працює в 4 
випадках:
якщо довжина рядка в дфапазоні 30-50 -> 
прінтує довжину, кількість букв та цифр
якщо довжина менше 30 -> 
прінтує суму всіх чисел та окремо рядок без цифр лише з буквами
якщо довжина бульше 50 - > ваша фантазія
звысно 4 все інше'''

def func(s):
    if(len(s) > 30 and len(s) < 50): #виводить довжину строки количество цифр и букв
        print("длина строки: " + str(len(s)))
        print("количество цифр: " + str(len([int(d) for d in s if d.isdigit()])))
        print("количество букв: " + str(len([str(d) for d in s if not d.isdigit()])))
        
    elif (len(s) < 30): #виводить суму цифр і строку без цифр
        mystr = ""
        mysum = 0
        numblist = [int(d) for d in s if d.isdigit()]
        for n in numblist:
            mysum = mysum + n
        print("Сумма: " + str(mysum))
        for d in s:
            if not d.isdigit():
                mystr = mystr + d
        print(mystr)
    elif (len(s) > 50): #виводить добуток чисел і строку великими
        mystr = ""
        product = 1
        numblist = [int(d) for d in s if d.isdigit()]
        for n in numblist:
            product = product * n
        print("Добуток: " + str(product))
        for d in s:
            if not d.isdigit():
                mystr = mystr + d
        print(mystr.upper())
    else:   #if string length = 30 or 50
        print("try again!")
         
st = input("enter your string: ")
func(st)
