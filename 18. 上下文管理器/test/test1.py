class GeneratorContextManager:
    def __init__(self,managed_resource):
        self.managed_resource = managed_resource

    def __enter__(self):
        return next(self.managed_resource)

    def __exit__(self, exc_type, exc, tb):
        try:
            next(self.managed_resource)
        except StopIteration:
            pass
        return False

def contextmanager(fac):
    def wap (*agrs):
        m = fac(*agrs)
        return GeneratorContextManager(m)
    return wap

## contextmanager(managed_resource)
@contextmanager
def managed_resource(name):
    """用生成器实现上下文管理器"""
    print(f"获取资源: {name}")
    resource = {"name": name, "status": "active"}
    try:
        yield resource  # yield 之前的代码等价于 __enter__
    finally:
        print(f"释放资源: {name}")  # yield 之后的代码等价于 __exit__


# 使用
with managed_resource("database") as res:
    print(f"使用资源: {res}")
# 获取资源: database
# 使用资源: {'name': 'database', 'status': 'active'}
# 释放资源: database



@contextmanager
def safe_file_write(file_path):
    """安全写入文件：先写入临时文件，成功后再替换原文件"""
    temp_path = file_path + ".tmp"
    print(temp_path)
    try:
        f = open(temp_path, "w")
        yield f
        f.close()
        # 写入成功，替换原文件

        import os
        os.replace(temp_path, file_path)
        print("写入成功")
    except Exception as e:
        # 写入失败，清理临时文件
        f.close()
        import os
        if os.path.exists(temp_path):
            os.remove(temp_path)
        print(f"写入失败: {e}")
        raise  # 重新抛出异常


# 使用
with safe_file_write("data.txt") as f:
    f.write("Hello, World!\n")
