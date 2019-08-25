# Factorial Function using Loop :-
def Factorial(n):
    fact = 1
    while n > 0:
        fact = fact * n
        n-=1
    return fact
#------------------------------------------------------------------------------------#
# Factorial Function using Recursion :-
def FactorialbyRecursion(n):
    if n == 1:
        return 1
    answer = n * FactorialbyRecursion(n-1)
    return answer        

print(FactorialbyRecursion(5))


    


