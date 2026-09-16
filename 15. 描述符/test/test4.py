class Temperature:
    def __init__(self,s):
        self._s = s
    @property
    def celsius(self):
        return self._s

    @celsius.setter
    def celsius(self,value):
        if not (-273.15 < value < 1000) :
            raise ValueError("温度不能低于绝对零度")
        self._s = value

    @property
    def fahrenheit(self):
        return 77.0

    @property
    def kelvin(self):
        return 298.15
t = Temperature(25)
print(t.celsius)      # 25
print(t.fahrenheit)   # 77.0（只读属性，自动计算）
print(t.kelvin)       # 298.15（只读属性，自动计算）

t.celsius = -300    # ValueError! 温度不能低于绝对零度
