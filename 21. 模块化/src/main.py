from my_package.module_a import *

print(member1)


def test():
    from my_package.module_b import member1

    print(member1)


test()


def test2():
    from my_package.module_b import member1

    print(member1)


test2()
