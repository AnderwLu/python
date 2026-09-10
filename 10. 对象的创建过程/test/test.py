class C:
    _v = None
    def __new__(cls):
        if cls._v is None:
            cls.v = super().__new__(cls)
        return cls._v

print(C() is C())