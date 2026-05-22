from contextlib import contextmanager


@contextmanager
def retry(max_attempts=3, exceptions=(Exception,)):
    attempt = 0
    while attempt < max_attempts:
        try:
            yield
            return  # 成功，直接返回
        except exceptions as e:
            attempt += 1
            if attempt >= max_attempts:
                raise  # 超过最大重试次数，重新抛出异常
            print(f"第 {attempt} 次尝试失败: {e}，准备重试...")


# 使用
attempt_count = 0


def unstable_function():
    global attempt_count
    attempt_count += 1
    if attempt_count < 3:
        raise ConnectionError("连接失败")
    return "成功"


with retry(max_attempts=3, exceptions=(ConnectionError,)):
    result = unstable_function()
    print(result)  # 成功（前两次失败自动重试）
