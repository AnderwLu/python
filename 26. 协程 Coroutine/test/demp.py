def ye():
    yield 2
    yield 3
    yield 4
    return "ok"


y = ye()


def run():
    try:
        y.send(None)
        run()
    except StopIteration as e:
        print(e.value)


run()
