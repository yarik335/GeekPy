# 3. Write a script to sum of the first n positive integers.

from random import randint
myArray = []
n = int(input("enter n: "))
summ = 0
ind = 0
for i in range(40):
    myArray.append(randint(-40,20))
print (myArray)      
for i in range(len(myArray)):  
    if(myArray[i] > 0 and ind < n):        
        print (myArray[i])  
        summ += myArray[i]
        ind += 1
print ("summ="+str(summ))  
