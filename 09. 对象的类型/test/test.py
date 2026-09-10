class P:
    p = "父类"
    def __init__(self,p1):
        self.p1 = p1
class Test(P):
    def __init__(self, owner, balance):
        super().__init__("给父类的")
        self.owner = owner          # 公有
        self._balance = balance     # 保护
        self.__password = "123456" 

t = Test("共用","保护")
print(t.owner)
print(t._balance)
print(t._Test__password)
print(t.__dict__)
print("---" * 40)
print(Test.__dict__)
print("---" * 40)
print(P.__dict__)
print("---" * 40)
print(t.p)
print(t.p1)
