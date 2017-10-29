# 6. Write a script to check whether a specified value is contained in a group of 
#    values. 
#         Test Data : 
#         3 -> [1, 5, 8, 3] : True
#         -1 -> (1, 5, 8, 3) : False
def Check(mylist,v):
    return print (v in mylist)
        
myList1 = [1, 5, 8, 3]
myList2 = (1, 5, 8, 3)
value = int(input("enter your value: "))
print(myList1)
Check(myList1,value)
print(myList2)
Check(myList2,value)
