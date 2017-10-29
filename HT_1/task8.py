# 8. Write a script to replace last value of tuples in a list. 
#         Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
#         Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
def replace(l,value):
    for i in range(len(l)):
        l[i]=l[i][:-1] + (value,)
    
myList = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
v = int(input("enter your value: "))
replace(myList, v)
print(myList)
#print(myList[0][-1])
