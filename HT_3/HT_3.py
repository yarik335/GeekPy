from random import randint
from random import uniform
import time

def list_int(*args):
    for i in range(0,1000):
            args[0].append(randint(0,99))
def list_float(*args):
    for i in range(0,1000):
        args[0].append(uniform(0,99))    
def sel_sort(mylist):
    for fillslot in range(len(mylist)-1,0,-1):#лен от -1 потому что
#счет идет от 0 а нам надо количество елементов в списке, до 0, -1 это шаг
        positionOfMax=0 # сначла позиция максимального 0
        for location in range(1,fillslot+1): # в этом цикле ищем 
            #максимальный елемент,fillslots +1 потому что он уже декрементировалься в первой итерации прошлого цикла а нам надо полное количество елементов списка
            # от 1 потому что в конце все равно останется 2 елемента и если условие сработает то они поменяются местами  
            if mylist[location]>mylist[positionOfMax]: 
                positionOfMax = location

        temp = mylist[fillslot]#заменяем местами максимальный и последний в неотсортированном месте списка
        mylist[fillslot] = mylist[positionOfMax]
        mylist[positionOfMax] = temp
    return mylist    
def ins_sort(mylist):
    for index in range(1,len(mylist)): #берем от 1 потому что будем 
        #проверяем со зачение слева
        value = mylist[index]
        i = index - 1
        while i >= 0:
            if value < mylist[i]: # если значение меньше значения слева 
                #заменяем местами
                mylist[i + 1] = mylist[i]
                mylist[i] = value
                i = i - 1 #декрементируем і и проверяем со значениями
                # еще левее
            else:
                break
                          
    return mylist
def bubble_sort(mylist):
  
    exchanges = True #если правда то заменяем
    passnum = len(mylist)-1 # количество елементов счет от 0
    while passnum > 0 and exchanges: # пока количество >0 и происходят замены
        exchanges = False # если нечего заменять
        for i in range(passnum): #проходим по всем неотсортированным елементам
            if mylist[i]>mylist[i+1]: #проверям текущий с правым елементом
                exchanges = True # будет замена
                mylist[i],mylist[i+1] = mylist[i+1],mylist[i]# замена через multiple assignments
        passnum = passnum-1 #декрементируем количество потому что один елемент уже на своем месте
    return mylist
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            
            gapInsertionSort(alist,startposition,sublistcount)
        sublistcount = sublistcount // 2
def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

listint =[]
listfloat =[]
listtmp = []
list_int(listint)
list_float(listfloat)
listintsort = list(listint)
listfloatsort = list(listfloat)
listintsort.sort()
listfloatsort.sort()

listtmp = list(listint)
start = time.process_time()
sel_sort(listtmp)
elapsed = time.process_time()
print("Egual to sort method:"+str(listintsort == listtmp),end = "")
print(", time of selection sort (list of integers):%0.4f" %((elapsed-start)*1000.0)+"ms")

listtmp = list(listfloat)
start = time.process_time()
sel_sort(listtmp)
elapsed = time.process_time()
print("Egual to sort method:"+str(listfloatsort == listtmp),end = "")
print(", time of selection sort (list of floats):%0.4f" %((elapsed-start)*1000.0)+"ms")



listtmp = list(listint)
start = time.process_time()
ins_sort(listtmp)
elapsed = time.process_time()
print("Egual to sort method:"+str(listintsort == listtmp),end = "")
print(", time of insertion sort (list of integers):%0.4f" %((elapsed-start)*1000.0)+"ms")

listtmp = list(listfloat)
start = time.process_time()
ins_sort(listtmp)
elapsed = time.process_time()
print("Egual to sort method:"+str(listfloatsort == listtmp),end = "")
print(", time of insertion sort (list of floats):%0.4f" %((elapsed-start)*1000.0)+"ms")

listtmp = list(listint)
start = time.process_time()
bubble_sort(listtmp)
elapsed = time.process_time()
print("Egual to sort method:"+str(listintsort == listtmp),end = "")
print(", time of bubble sort (list of integers):%0.4f" %((elapsed-start)*1000.0)+"ms")

listtmp = list(listfloat)
start = time.process_time()
bubble_sort(listtmp)
elapsed = time.process_time()
print("Egual to sort method:"+str(listfloatsort == listtmp),end = "")
print(", time of bubble sort (list of floats):%0.4f" %((elapsed-start)*1000.0)+"ms")

listtmp = list(listint)
start = time.process_time()
shellSort(listtmp)
elapsed = time.process_time()
print("Egual to sort method:"+str(listintsort == listtmp),end = "")
print(", time of Shell sort (list of integers):%0.4f" %((elapsed-start)*1000.0)+"ms")

listtmp = list(listfloat)
start = time.process_time()
shellSort(listtmp)
elapsed = time.process_time()
print("Egual to sort method:"+str(listfloatsort == listtmp),end = "")
print(", time of Shell sort (list of floats):%0.4f" %((elapsed-start)*1000.0)+"ms")
"""
Output 100000 elements:
Egual to sort method:True, time of selection sort (list of integers):439642.9257ms
Egual to sort method:True, time of selection sort (list of floats):519203.8982ms
Egual to sort method:True, time of insertion sort (list of integers):514850.7305ms
Egual to sort method:True, time of insertion sort (list of floats):551076.8242ms
Egual to sort method:True, time of bubble sort (list of integers):969604.5589ms
Egual to sort method:True, time of bubble sort (list of floats):1050730.5736ms
Egual to sort method:True, time of Shell sort (list of integers):586.7913ms
Egual to sort method:True, time of Shell sort (list of floats):1059.9721ms"""