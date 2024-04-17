l =[12,23,45,12,78,89]
n=len(l)
target=12
result=0
for index in range(n):
    if l[index]==target:
        result=result+1
print(result)
