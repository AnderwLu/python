class property:
    def __init__(self,fget = None,fset = None,fdel = None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance,value)

    def __delete__(self, instance):
        self.fdel(instance)

    def setter (self,fset):
        return property(self.fget,fset)
    def deleter(self,fdel):
        return property(self.fget,self.fset,fdel)

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """获取半径"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """设置半径，带验证"""
        if value < 0:
            raise ValueError("半径不能为负数")
        self._radius = value

    @radius.deleter
    def radius(self):
        """删除半径"""
        print("删除半径")
        del self._radius

    @property
    def area(self):
        """计算面积（只读属性）"""
        import math
        return math.pi * self._radius ** 2

    @property
    def diameter(self):
        """计算直径（只读属性）"""
        return self._radius * 2


c = Circle(5)
print(c.radius)     # 5 —— 调用 getter
print(c.area)       # 78.54... —— 自动计算
print(c.diameter)   # 10

c.radius = 10       # 调用 setter
print(c.area)       # 314.15...

# c.area = 100      # AttributeError! area 没有 setter
# c.radius = -5     # ValueError! 半径不能为负数

# del c.radius      # 调用 deleter
# print(c.radius)   # AttributeError!


def aa():
    return 5

print(aa)