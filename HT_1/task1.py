# 1 .Write a script which accepts a sequence of comma-separated numbers from user and
#  generate a list and a tuple with those numbers. 
#         Sample data : 1, 5, 7, 23
#         Output : 
#         List : [‘1', ' 5', ' 7', ' 23'] 
#         Tuple : (‘1', ' 5', ' 7', ' 23')
i = input("input comma-seperated numbers:")
l = i.split(sep = ',')
t = tuple(l)
print(l)
print(t)

#print(i.split(sep=','))
#print(tuple(i.split(sep=',')))
