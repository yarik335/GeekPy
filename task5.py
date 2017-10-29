# 5. Write a script to convert decimal to hexadecimal
#         Sample decimal number: 30, 4
#         Expected output: 1e, 04
def ChangeHex(n):
    print (hex(n).split('x')[-1])
    
num = input("enter decimal numbers (comma separated): ")
numbers = num.split(sep = ',')
for i in range(len(numbers)):
    ChangeHex(int(numbers[i]))