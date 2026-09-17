class SuppressError:
    """忽略指定类型的异常"""
    
    def __init__(self, *exception_types):
        self.exception_types = exception_types

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None and issubclass(exc_type, self.exception_types):
            print(f"捕获并忽略异常: {exc_type.__name__}: {exc_val}")
            return True  # 返回 True，异常被处理，不再传播
        return False  # 不处理其他异常


# 使用
with SuppressError(ZeroDivisionError):
    result = 1 / 0  # 不会报错
    print("这行不会执行")

print("程序继续执行")  # 正常执行


class DatabaseConnection:
    def __init__(self, host):
        self.host = host
        self.connected = False

    def __enter__(self):
        """进入 with 块时调用，返回的对象赋值给 as 后的变量"""
        print(f"连接到数据库: {self.host}")
        self.connected = True
        return self  # 返回自身，供 with 块使用

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        离开 with 块时调用
        exc_type: 异常类型（无异常时为 None）
        exc_val: 异常值
        exc_tb: 异常追踪信息
        返回 True 表示异常已处理，不再向上传播
        """
        print(f"关闭数据库连接: {self.host}")
        self.connected = False
        return False  # 返回 False，不处理异常，让异常继续传播

    def query(self, sql):
        if not self.connected:
            raise RuntimeError("未连接到数据库")
        print(f"执行查询: {sql}")
        return ["result1", "result2"]


# 使用上下文管理器
with DatabaseConnection("localhost") as conn:
    print(f"连接状态: {conn.connected}")  # True
    results = conn.query("SELECT * FROM users")
    print(results)

# 离开 with 块后
print(f"连接状态: {conn.connected}")  # False
