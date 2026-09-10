class Dog:
    age = "29"
    def __init__(this,add):
        this.add = add
        print( add + Dog.age)

    def addm(this,name):
        print(name + Dog.age)

    @classmethod
    def cls(cls, int):
        print(cls.age + int)
        dog = Dog("79")
        cls.addm(dog,"gondu")

    @staticmethod
    def sta(n,x):
        print(n * x)
# 实列调用三个方法
dog = Dog("78")
dog.addm("add")
dog.cls("0000")
dog.sta(2,3)

# 类调用
Dog.addm(Dog("100"),"100")
Dog.cls("900")
Dog.sta(5 , 5)

print(Dog.__mro__)

print(dog.__dict__)  
print(Dog.__dict__)  



# 查看对象的所有属性和方法
print("=" * 50)
print(dir(dog))

# 查看类的所有属性和方法
print("=" * 50)
print(dir(Dog))
print("=" * 50)
print(dir())