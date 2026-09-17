def generator():
    print("准备 yield 1")
    yield 1
    print("准备 yield 2")
    yield 2
    print("准备 yield 3")
    yield 3
    print("生成器结束")


g = generator()
print("生成器已创建") # 生成器已创建
print(next(g)) # 准备 yield 1. 1
print("---") # ("---")
print(next(g)) # 准备 yield 2  2
print("---")# ("---")
g.close()
print("生成器已关闭") # 生成器已关闭
print(next(g))
