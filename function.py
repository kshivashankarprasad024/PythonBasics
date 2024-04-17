print("Hello Function")

def solveIt2():
    print("This is FIRST Line getting executed")
    print("This is line 123")

print("I am not getting PRINTED")

def solveIt4():
    print("Iam solveIt4")
    print("This is getting executed")
    solveIt2()
    print("Second line is getting executed")

def solveIt():
    print("This is line 111")
    print("This is line 112")
    solveIt4()
    print("SolveIt4 haven't completed its execution")

def sumOfTwoNumbers(num1, num2):
    print("After execution")
    solveIt()
    print("Nothing gets printed")
    result = num1 + num2
    print("Before execution")
    return result

print("Last line is getting printed")
num1 = int(input())
num2 = int(input())
result = sumOfTwoNumbers(num1, num2)
print(result)
