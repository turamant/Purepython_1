class Rest:
    pass

def add_attribute(self):
    self.z = 9

class Foo:
    def show(self):
        print("hello foo")


print(type(Rest), Rest)
print(type(int), int)


Test = type('Test', (Foo, Rest,), {"x": 5, "add_attribute": add_attribute})  # main
t1 = Test()
t1.wy = "hello"
print(t1.x, t1.wy)
t1.show()
t1.add_attribute()
print(t1.z)
