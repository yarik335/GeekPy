# 7. Write a script to concatenate all elements in a list into a string and print it.
myList = input("enter your list: ")
myList = myList.split(sep = ',')
print(myList)
print("".join(myList))