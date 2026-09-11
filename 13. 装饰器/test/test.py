def fibonacci(n):
    if n < 2:
        return n
    print(f"{n -1 + n -2}")
    return fibonacci(n - 1) 

print(fibonacci(35))  # 应该快速返回结果