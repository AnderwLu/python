class A:
    def __call__(self):
        print("A called")

class B(A):
    def __call__(self):
        print("B called")
        super().__call__()

b = B()
b()
# B called
# A called
"""
一、实现一个计数器类
编写一个 Counter 类：

初始化时指定起始值
每次调用实例，计数器值加 1
支持 reset() 方法重置为初始值
支持 get() 方法获取当前值
c = Counter(10)
print(c())      # 11
c()             # 12
print(c.get())  # 12
c.reset()
print(c.get())  # 10
"""

class Counter:
    def __init__(self,count):
        self.init = count
        self.count = count

    def __call__(self, *args, **kwds):
        self.count += 1
        return self.count

    def reset(self):
        self.count = self.init

    def get(self):
        return self.count

c = Counter(10)
print(c())      # 11
print(c())      # 12
print(c.get())  # 12
c.reset()
print(c.get())  # 10