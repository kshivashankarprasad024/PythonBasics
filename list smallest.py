def findsmallest(numbers):
    result=1233833829383
    n=len(numbers)
    for index in range(n):
        if numbers[index] <result:
            result=numbers[index]
    return result

numbers=[12,3,56,78,90,6666,1,2,7]
result=findsmallest(numbers)
print("smallest is",result)    
    
