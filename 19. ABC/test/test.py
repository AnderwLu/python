from abc import ABC, abstractmethod
from contextlib import contextmanager
import json

class Cache(ABC):
    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def set(self, key, value):
        pass

    @abstractmethod
    def delete(self, key):
        pass

# 实现 MemoryCache（使用字典存储）
# 实现 FileCache（使用文件存储）


class MemoryCache(Cache):
    map = {}
    def get(self, key):
        return MemoryCache.map.get(key)
    
    def set(self, key, value):
        MemoryCache.map[key] = value

    def delete(self, key):
        del MemoryCache.map[key]

me = MemoryCache()
me.set("abc",233)
print(me.get("abc"))
me.delete("abc")
print(me.get("abc"))

class FileCache(Cache):
    def __init__(self):
        super().__init__()
        self.data = "data.txt"
    @contextmanager
    def safe_file_write(self):
        try:
            f = open(self.data, "r+", encoding="utf-8")
            yield f
        finally:
            f.close()

    def get(self, key):
        with self.safe_file_write() as f:
            str = f.read()
            data = json.loads(str) if str else {}
            return data.get(key)
        
    def set(self, key, value):
        with self.safe_file_write() as f:
            str = f.read()
            data = json.loads(str) if str else {}
            data[key] = value
            f.seek(0)       # 指针回到文件开头
            f.truncate()    # 清空文件
            f.write(json.dumps(data, ensure_ascii=True))

    def delete(self, key):
        with self.safe_file_write() as f:
            str = f.read()
            data = json.loads(str) if str else {}
            del data[key]
            f.seek(0)       # 指针回到文件开头
            f.truncate()
            f.write(json.dumps(data, ensure_ascii=True))

fel = FileCache()
fel.set("aba",124)
fel.set("abc",124)
fel.set("ab5",124)
fel.set("ab6",124)
print(fel.get("aba"))

