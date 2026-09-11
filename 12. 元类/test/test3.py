''' 解题思路：
1. call负责的是创建实列的行为，这里是实例调用方法，实例已经创建完成，且所有实例方法都用共同特征所以判断是创建行为
2. init 和 new 函数都可以找到需要操作的函数，但是需要注意这里函数调用找的类对象里的__dict__不是实例里的__dict__
3. 经验一般new修改添加类行为属性，init校验登记类属性
'''
class LogMeta(type):
    # 你的代码
    def __new__(cls, name, bases, dict, /, **kwds):
        for k,v in dict.items():
            if not k.startswith("_") and callable(v):
                dict[k] = cls.log_wrapper(v)
        return super().__new__(cls,name, bases, dict, **kwds)


    @staticmethod
    def log_wrapper(v):
        def log (*args,**k):
            print(f"[LOG] 调用 {k}")
            return v(*args,**k)
        return log
class Calculator(metaclass=LogMeta):
    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b

calc = Calculator()
print(calc.__dict__)
print(Calculator.__dict__)
print(calc.add(3, 5))
print(calc.sub(10, 4))

# 应该输出：
# [LOG] 调用 add
# 8
# [LOG] 调用 sub
# 6
