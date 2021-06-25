from queue import Queue as q
import inspect


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person({self.name})"

    def __mul__(self, other):
        if type(other) is not int:
            raise Exception("Invalid arguments, must be int")
        self.name = self.name * other

    def __call__(self, *args, **kwargs):
        return f"calling method", args

    def __len__(self):
        return len(self.name)

class Queue(q):
    def __repr__(self):
        return f"Queue({self._qsize()})"

    def __add__(self, other):
        self.put(other)

    def __sub__(self, other):
        self.get()

p = Person("Klim")

print(p)
print(p(1,6,8))
print(len(p))

print(12*"=")

qu = Queue()
qu + 9
qu + 7
qu - None
print(qu)