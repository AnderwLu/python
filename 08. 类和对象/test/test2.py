class Animal:
    kingdom = "Animalia"

    def __init__(self, name):
        self.name = name

class Dog(Animal):
    count = 0

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        Dog.count += 1

    def bark(self):
        return f"{self.name} says Woof!"

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(type(dog1)) # __class_.Dog
print(type(Dog)) # type
print(isinstance(dog1, Animal)) # true
print(isinstance(dog1, (int, Dog))) # true
print(issubclass(Dog, object)) # true
print(dog1.__class__.__name__) # Dog
print(Dog.__base__.__name__) # Animal
print(hasattr(dog1, "kingdom")) # true
print(getattr(dog1, "age")) # 3
print(getattr(dog2, "color", "brown")) # brown
setattr(dog1, "color", "golden")
print(dog1.color) # golden
print("bark" in dir(dog1)) # true
setattr(dog2, "color", "golden2")
print(vars(dog2)) # {'name': 'Max', 'age': 5}
delattr(dog1, "color")
print(hasattr(dog1, "color")) # false
print(Dog.count) # 2
