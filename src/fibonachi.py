"""
fibonachi

"""
def fibo(n):
    return 1 if n <= 2 else fibo(n-1) + fibo(n-2)

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    cur = 1
    if n > 2:
        cur = fibonacci(n-1) + fibonacci(n-2)
    return cur

def fib_row(n):
    row = []
    for i in range(1, n+1):
        k = fibonacci(i)
        row.append(k)
    return row

if __name__=='__main__':
    print(fibo(10))
    print(fib(10))
    print(fibonacci(10))
    n_row = fib_row(10)
    print("Ряд: ", n_row)
    print("Сумма: ", sum(n_row))