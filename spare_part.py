class Supplier:
    def __init__(self, vendor, name):
        self._vendor = vendor
        self._name = name


test = Supplier("a", "s")
print(test._vendor)
