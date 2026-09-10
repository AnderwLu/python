function = type(lambda: None)

# type
print("type(type)", type(type)) # type
print("isinstance(type, type)", isinstance(type, type)) # true
print("isinstance(type, function)", isinstance(type, function)) # false
print("isinstance(type, object)", isinstance(type, object)) # true
print("\n")

# object
print("type(object)", type(object)) # type
print("isinstance(object, type)", isinstance(object, type)) # true
print("isinstance(object, function)", isinstance(object, function))  # false
print("\n")

# function
print("type(function)", type(function)) # type
print("isinstance(function, object)", isinstance(function, object))  # true
print("isinstance(function, type)", isinstance(function, type))  # true
print("isinstance(function, function)", isinstance(function, function))  # false
print("\n")


# 普通对象和类
class A:
    pass


a = A()
print("type(a)", type(a)) # A
print("type(A)", type(A)) # type
print("isinstance(A, A)", isinstance(A, A))  # false
print("isinstance(A, object)", isinstance(A, object))  # true
print("isinstance(A, type)", isinstance(A, type)) # true
print("isinstance(A, function)", isinstance(A, function))  # false
print("isinstance(a, A)", isinstance(a, A)) # true
print("isinstance(a, object)", isinstance(a, object)) # true
print("isinstance(a, type)", isinstance(a, type)) # false
print("isinstance(a, function)", isinstance(a, function)) # false
print("\n")


# 普通函数
def func():
    pass


print("type(func)", type(func))  # function
print("isinstance(func, object)", isinstance(func, object)) # true
print("isinstance(func, type)", isinstance(func, type)) # false
print("isinstance(func, function)", isinstance(func, function))  # true
print("\n")
