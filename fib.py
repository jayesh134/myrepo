n1 = 0
n2 = 1
def fib(n):
    if n==n1 or n==n2:
        return n
    
    return fib(n-1) + fib(n-2)

print(fib(6))