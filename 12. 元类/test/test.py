class O(type) :
    # O类创建“类对象 P”
    # P = __new__(O,P,(B),P的命名空间)
    def __new__(cls, name, bases, namespace, /, **kwds):
        print(f"谁 {cls} ,创建了 {name} 类，父类是 {bases} , 命名空间 {namespace} , 参数是 {kwds}")
        return super().__new__(cls,name, bases, namespace, **kwds)
    # 初始化“类对象 P”
    # O.__init__(P,"P",(B),P的命名空间)
    def __init__(self, name, bases, dict, /, **kwds):
        print (f"谁 {self} - {name} 开始初始化, 父类是 {bases} , 参数是 {dict}")
        super().__init__(name, bases, dict, **kwds)
    # 调用“类对象 P”，创建并初始化 P 的实例

    def __call__(self, *args, **kwds):
        print(f"{self} 被实例化了，参数是 {args} -- {kwds}")
        return super().__call__(*args, **kwds)

class B:
    pass

# class P(B,metaclass=O) 本质是语法糖，实际 == ”P = __new__(O,P,(B),P的命名空间) + O.__init__(P,"P",(B),P的命名空间)“
class P(B,metaclass=O):
    def __init__(self,name):
        super().__init__()
        self.name = name
# O.__call__(P, "name") == P("name")
p = P("name")