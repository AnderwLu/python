from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def foo(self):
        pass

    def bar(self):
        print("A.bar")

class B(A):
    def foo(self):
        print("B.foo")

class C(B):
    pass

c = C() 
c.foo() # B.foo
c.bar() # A.bar

class D(A):
    pass

d = D()