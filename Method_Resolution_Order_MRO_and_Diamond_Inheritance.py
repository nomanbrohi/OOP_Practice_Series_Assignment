class A():
    def show(self):
        print("class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

obj1 = D()

obj1.show()
print(D.mro())
