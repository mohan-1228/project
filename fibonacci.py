def Fibonacci(n):
    if n< 0:
        print("Incorrect input!! Please input numbers greater or equal to 0")
    
    elif n == 0:
        return 1
    
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 

i = int(input("enter a number ") )
print(Fibonacci(i))
 




