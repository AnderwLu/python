import math
class RadiusDescriptor:
    def __get__(self, instance, owner):
        return instance._radius

    def __set__(self, instance, value):
        if value < 1:
            raise ValueError("半径不能小于0")
            
        instance._radius = value

class AreaDescriptor:
    def __set__(self, instance, value):
        raise AttributeError("只读的属性")

    def __get__(self, instance, owner):
        return instance.radius ** 2 * math.pi

class DiameterDescriptor:
    def __set__(self, instance, value):
        raise AttributeError("只读的属性")
    
    def __get__(self, instance, owner):
        return instance.radius * 2
class Circle:
    radius = RadiusDescriptor()
    area = AreaDescriptor()
    diameter = DiameterDescriptor()

    def __init__(self, radius):
        self.radius = radius


c1 = Circle(5)  # 没问题
print(c1.radius)  # 输出 5
print(c1.area)  # 输出 78.53981633974483
print(c1.diameter)  # 输出 10
c1.radius = 10  # 没问题
print(c1.radius)  # 输出 10
print(c1.area)  # 输出 314.1592653589793
print(c1.diameter)  # 输出 20

print(c1.__dict__)
c1.area = 100  # 报错
print(c1.area)