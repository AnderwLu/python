# fibonacci = cache(fibonacci)
def cache(func):
    map = {}
    def wrapper (n):
        if n in map:
            ## 判断这个数已经计算过了就直接返回不要计算
            return map[n]
        ## 没计算过开始计算并缓存
        rs = func(n)
        map[n] = rs
        return rs
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(35))  # 应该快速返回结果

