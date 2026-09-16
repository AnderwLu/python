import math
from functools import total_ordering
@total_ordering
class Fraction:
    def __init__(self,x,y):
        g = math.gcd(abs(x), abs(y))
        self.x = x // g
        self.y = y // g

    
    def __add__(self, other):
        """
        加法逻辑：

        1. 第一个分数的分子乘以第二个分数的分母
        2. 第二个分数的分子乘以第一个分数的分母
        3. 将上面两个结果相加，得到新分子
        4. 两个分数的分母相乘，得到新分母
        5. 使用新分子和新分母创建一个新的分数对象
        6. 新分数需要进行约分

        """
        if not isinstance(other, Fraction):
            return NotImplemented
        newx = self.x  * other.y + other.x * self.y
        newy = self.y * other.y
        return Fraction(newx,newy)

    def __sub__(self, other):
        """减法逻辑：
        1. 第一个分数的分子乘以第二个分数的分母
        2. 第二个分数的分子乘以第一个分数的分母
        3. 用第一个结果减去第二个结果，得到新分子
        4. 两个分数的分母相乘，得到新分母
        5. 使用新分子和新分母创建一个新的分数对象
        6. 新分数需要进行约分"""
        if not isinstance(other,Fraction):
            return NotImplemented
        newx = self.x  * other.y - other.x * self.y
        newy = self.y * other.y
        return Fraction(newx,newy)
    def __mul__(self, other):
        """乘法逻辑：
        1. 两个分数的分子相乘，得到新分子
        2. 两个分数的分母相乘，得到新分母
        3. 使用新分子和新分母创建一个新的分数对象
        4. 新分数需要进行约分"""
        if not isinstance(other,Fraction):
            return NotImplemented
        newx = self.x * other.x
        newy = self.y * other.y
        return Fraction(newx,newy)
    def __truediv__(self, other):
        """除法逻辑：
        1. 检查第二个分数的分子是否为 0
        2. 如果为 0，说明正在除以 0，应当报错
        3. 将第二个分数的分子和分母交换，相当于取倒数
        4. 第一个分数的分子乘以第二个分数的分母，得到新分子
        5. 第一个分数的分母乘以第二个分数的分子，得到新分母
        6. 使用新分子和新分母创建一个新的分数对象
        7. 新分数需要进行约分
        """
        if not isinstance(other,Fraction):
            return NotImplemented
        if self.x == 0 or other.x == 0:
            raise NotImplementedError
        newx = self.x * other.y
        newy = self.y * other.x
        return Fraction(newx,newy)
    def __eq__(self, other):
        if not isinstance(other,Fraction):
            return NotImplemented
        return self.x == other.y and self.y == other.x
        
    def __lt__(self, other):
        if not isinstance(other,Fraction):
            return NotImplemented
        newx = self.x * other.y
        newy = self.y * other.x
        print(f"测试的 {newx} - {newy} -{newx > newy}")
        return newx < newy

    def __float__(self):
        return self.x / self.y

    def __str__(self):
        return f"{self.x}  / {self.y}"

    def __repr__(self):
        return f"Fraction({self.x}, {self.y})"

f1 = Fraction(1, 2)   # 1/2
f2 = Fraction(1, 3)   # 1/3

print(f1 + f2)        # 5/6
print(f1 - f2)        # 1/6
print(f1 * f2)        # 1/6
print(f1 / f2)        # 3/2
print(f1 == f2)       # False
print(f1 > f2)        # True
print(float(f1))      # 0.5
print(str(f1))        # "1/2"
print(repr(f1))       # "Fraction(1, 2)"
