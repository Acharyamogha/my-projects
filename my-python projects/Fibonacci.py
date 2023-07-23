def fib(n):
    if n<=0:
        raise ValueError("Input value should be greater than 0")
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

try:
    n=int(input("Enter a value "))
    res=fib(n)
    print(f"the {n}th term in the Fibonacci sequence is: {res}")
except ValueError as e:
    print("Error", e)
