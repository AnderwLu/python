class FibonacciIterator:
    """无限斐波那契数列迭代器"""

    def __init__(self):
        self.a = 1
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        n = self.a
        self.a,self.b = self.b,self.a + self.b
        return n

fib = FibonacciIterator()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

class Countdown:
    def __init__(self,int):
        self.int = int

    def __iter__(self):
        return CountdownIterator(self.int)

class CountdownIterator:
    def __init__(self,int):
        self.int = int

    def __iter__(self):
        return self

    def __next__(self):
        if self.int < 0:
            raise StopIteration
        num = self.int
        self.int -= 1
        return num

for i in Countdown(4):
    print(i)