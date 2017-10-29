"""(таких ф-цій потрібно написати 3 -> різними варіантами) Написати функцію season,
 приймаючу 1 аргумент — номер місяця (від 1 до 12), яка буде повертати пору року, якій 
 цей місяць належить (зима, весна, літо або осінь)."""
 
 
 
def season1(k):
    #1 method with dictionaries

    return {12:"winter",1:"winter",2:"winter",3:"spring",4:"spring",5:"spring",6:"summer",7:"summer",8:"summer",9:"Fall",10:"Fall",11:"Fall"}.get(k,"введите корректный номер месяца")

    #2 method with dictionaries
    """if (k in (1,2,12)):
        k = (12,1,2)
        
    elif (k in (3,4,5)):
        k = (3,4,5)
        
    elif (k in (6,7,8)):
        k = (6,7,8)
    else: 
        k = (9,10,11)
        return {(1,2,12):"winter",(3,4,5):"spring",(6,7,8):"summer",(9,10,11):"Fall"}.get(k,"введите корректный номер месяца")

        """
    #3 method with dictionaries
    
"""   dic = {(1,2,12):"winter",(3,4,5):"spring",(6,7,8):"summer",(9,10,11):"Fall"}
     for key,v in dic.items(): 
         if(k in key): return v
     return "введите корректный номер месяца" 
   """  
    
def season2(k):
    if (k in (1,2,12)):
        return "Winter"       
    elif (k in (3,4,5)):
        return "Spring"
        
    elif (k in (6,7,8)):
        return "Summer"
    elif (k in (9,10,11)):
        return "Fall"
        
    else: 
        return "Введите корректный номер месяца"
    
def season3(k):
    winter = {1,2,12}
    spring = {3,4,5}
    summer = {6,7,8}
    autumn = {9,10,11}
    if (k in winter): return "winter"
    if (k in spring): return "spring"
    if (k in summer): return "summer"
    if (k in autumn): return "autumn"
    return "enter correct month number"

k = int(input("введите номер месяца: "))

print(season1(k))
print(season2(k))
print(season3(k))