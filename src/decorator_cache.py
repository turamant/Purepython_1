"""
decorator for cashing
"""

def decorator_caching(func, *args):
    cache = {}
    def wrapper(*args):
        print("-" * 50)
        print("Аргументы: ", *args)
        print("Кеш: ", cache)
        if cache.get(args):
            return cache[args]
        else:
            cache[args] = func(*args)
            return cache[args]
    return wrapper

@decorator_caching
def add(x, y):
    return x * y

if __name__=="__main__":
    while True:
        integer1 = int(input("Введите первый аргумент для сложения: "))
        if integer1 == -1:
            break
        integer2 = int(input("Введите второй аргумент для сложения: "))

        print(add(integer1, integer2))
