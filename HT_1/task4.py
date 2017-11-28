# 4. Write a script to concatenate N strings.
n = int(input("enter n: "))
s1 = []
s2 = []
s3 = []
for i in range(n):
    s1.append("hello ")
    s2.append("world")
for i in range(n):
    s3.append(s1[i]+s2[i])
    
print (s1)
print (s2)
print (s3)