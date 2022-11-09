# Factorial
def factorial(n) -> int:
    factorial=1
    if not isinstance(n, int):
        print('just integer')
        return None
    elif n < 0:
        print('Sorry, factorial does not exist for negative numbers')
        return None
    elif n == 0:
        return 1
    else:
        for i in range(1,n + 1):
            factorial = factorial*i
        print("The factorial of",n,"is",factorial)


# Fibonacci
def fibonacci(n: int) ->int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)