# using Recursion :-
def FibonacciRecursion(n):
    #list = [0,1]
    answer = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        answer = FibonacciRecursion(n-1) + FibonacciRecursion(n-2)
        return answer

print(FibonacciRecursion(36))
#-------------------------------------------------------------------------------------#
# using iterating approach: O(2^N)
def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1    
    previous = 0
    after = 1
    while n >= 2:
        answer = previous + after
        previous = after
        after = answer
        n-=1
    return answer

#print(Fibonacci(10))

         




    

