# 11. Write a script to remove duplicates from Dictionary.
dic1 = {1:10, 2:20,3:30, 4:40,5:20,6:60,7:20}
result = {}

for key,value in dic1.items():
    if value not in result.values():
        result[key] = value
print(result)