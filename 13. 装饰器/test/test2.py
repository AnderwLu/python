# 实现wraps装饰器，用于不改变函数的名称和注释
# 解题思路： 
# 1. say_hello = my_decorator（say_hello）
# 2. wrapper = wraps(func)(wrapper)
def wraps(func):
    def aa(a):
        print(f"ddddd {a}")
        def wra (wrapper):
            wrapper.__name__ = func.__name__
            wrapper.__doc__ = func.__doc__
            print(f"修改完成 {a}") 
            return wrapper
        return wra
    return aa


def my_decorator(func):
    @wraps(func)(10)
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")

    return wrapper


@my_decorator
def say_hello():
    """打招呼"""
    print("Hello!")


say_hello()
# 输出：
# 函数执行前
# Hello!
# 函数执行后
print("name", say_hello.__name__)
print("doc", say_hello.__doc__)
