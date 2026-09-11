import time

def timer(func):
    # 你的代码
    def ru (*args,**w):
        st = time.time()
        rs = func(*args,**w)
        print(f"{func.__name__} 执行时间:  {(time.time() - st):4f}:秒")
        return rs
    return ru

@timer
def slow_function():
    time.sleep(1)
    return "Done"

slow_function()
# 输出：
