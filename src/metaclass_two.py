class Meta(type):
    def __new__(cls, *args, **kwargs):
        print("Arguments^ ", args)
        return type(*args, **kwargs)

class Meta_two(type):
    def __new__(self, class_name, bases, attrs):
        print("Attributs: ", attrs)
        a = {}
        for key, value in attrs.items():
            if key.startswith("__"):
                a[key] = value
            else:
                a[key.upper()] = value
        return type(class_name, bases, a)

class Dog(metaclass=Meta):
    x = 5
    y = 8
    def hello(self):
        print("hello doggy!" )

class Cat(metaclass=Meta_two):
    x = 99
    y = 100
    def hello(self):
        print("hi , cat")

print(12*"=")
dog = Dog()
print(dog)
print(dog.x, dog.y)
print(12*"=")
cat = Cat()
print(cat)
print(cat.X, cat.Y)
cat.HELLO()