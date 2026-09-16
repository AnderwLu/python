class LazyProperty:
    """惰性加载属性：只在第一次访问时计算"""
    
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = self.func(instance)
        # 将结果缓存到实例的属性中
        setattr(instance, self.name, value)
        return value
    def __delete__(self, instance):
        pass
    def __set__(self, instance, value):
        pass


class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    @LazyProperty
    def data(self):
        print(f"正在加载文件: {self.file_path}")
        # 模拟耗时操作
        return [1, 2, 3, 4, 5]


loader = DataLoader("data.txt")
print(loader.__dict__)
print(loader.data)  # 正在加载文件: data.txt
                    # [1, 2, 3, 4, 5]
print(loader.data)  # [1, 2, 3, 4, 5] —— 不再加载，直接从属性读取
print(loader.__dict__)