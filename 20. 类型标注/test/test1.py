from typing import TypeVar, Generic, Optional

K = TypeVar("K")
V = TypeVar("V")


class Cache(Generic[K, V]):
    """泛型缓存类"""
    
    def __init__(self) -> None:
        # 你的代码
        self.map:dict[K,V] = {}
    
    def set(self, key: K, value: V) -> None:
        """设置缓存"""
        # 你的代码
        self.map[key] = value
    
    def get(self, key: K) -> Optional[V]:
        """获取缓存，不存在返回 None"""
        # 你的代码
        return self.map.get(key,None)
    
    def clear(self) -> None:
        """清空缓存"""
        # 你的代码
        self.map = {}


# 测试
cache: Cache[str, int] = Cache()
cache.set("a", 1)
cache.set("b", 2)
print(cache.get("a"))   # 1
print(cache.get("c"))   # None
cache.clear()
