class Base(object):
    def __init__(self):
        print("enter Base")
        print("leave Base")

class A(Base):
    def __init__(self):
        print("enter A")
        super().__init__()
        print("leave A")

class B(Base):
    def __init__(self):
        print("enter B")
        super().__init__()
        print("leave B")

class C(A, B):
    def __init__(self):
        print("enter C")
        super().__init__()
        print("leave C")

c = C()
## 注意这里不是按照类上的继承判断的，是按照创建实列的MRO顺序创建的，这里创建的是C，所以是C，A,B，Base
# enter C
# enter A
# enter B
# enter Base
# leave Base
# leave B
# leave A
# leave C