class newClass:
    def __new__(cls):
        print ("__new__ magic method is called")
        inst = object.__new__(cls)
        return inst
    def __init__(self):
        print ("__init__ magic method is called")
        self.name='Satya'
        """print(self.name)
        print(type(self))
        print(self.__dir__())
"""
    def __str__(self):
        return "I'm Overrided Version of base Str"

persoan = newClass()
print(persoan)