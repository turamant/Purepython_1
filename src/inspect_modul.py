import inspect
from queue import Queue


def func(x):
    if x == 1:
        def rv():
            print("X = 1")
    else:
        def rv():
            print("X not 1")
    return rv


new_func = func(1)
print(inspect.getmembers(new_func))
old_func = func(21)
print(inspect.getsource(old_func))

print(inspect.getsource(Queue))