def findgreatest(numbers):
    result=0
    n=len(numbers)
    for index in range(n):
        if numbers[index] > result:
            result=numbers[index]
    return result

numbers=[12,3,56,78,90,6666,1,2,7]
result=findgreatest(numbers)
print("greatest element is",result)   


