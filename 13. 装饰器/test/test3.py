# say_hello = repeat(3)(say_hello)
def repeat(n):
    # 你的代码
    def repeatf(say_hello):
        def run (*args):
            i = 0
            while i < n:
                say_hello(*args)
                i += 1
        return run
    return repeatf


@repeat(3)
def say_hello(s):
    print(s)


say_hello(1)  # 输出: 1 1 1
