class SingletonMeta(type):
    map = {}

    def __call__(self, *args, **kwds):
        print(self)
        if self not in self.map:
            p = super().__call__(*args, **kwds)
            self.map[self] = p
        print(str(self.map))
        return self.map[self]


class Database(metaclass=SingletonMeta):
    def __init__(self, host):
        self.host = host

db1 = Database("localhost")
db2 = Database("remote")
print(db1 is db2)  # 应该输出 True
print(db1.host)    # 应该输出 localhost