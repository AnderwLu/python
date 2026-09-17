from contextlib import contextmanager
import time

@contextmanager
def timer(str):
    star = time.time()
    yield 
    print(f"数据处理 耗时: {time.time() - star:.2f} 秒")
# 使用
with timer("数据处理"):
    time.sleep(1)
    print("处理完成")
# 处理完成
# 
from pathlib import Path
class TempDirectory:
    def __init__(self):
        pass
    def __enter__(self):
        self.path = Path("./test33")
        self.path.mkdir(parents=True, exist_ok=True)
        return self.path

    def __exit__(self, exc_type, exc, tb):
        self.path.rmdir()
        return False


with TempDirectory() as tmp_dir:
    print(f"临时目录: {tmp_dir}")
    # 可以在这个目录中创建文件
    # 离开 with 块时，目录及其内容自动删除

print("临时目录已清理")
