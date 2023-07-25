class Supplier:
    def __init__(self, vendor, brand, name, quantity, price, multiplicity, initial_row, markup, delivery_time, supp_num):
        self._vendor = vendor
        self._brand = brand
        self._name = name
        self._quantity = quantity
        self._price = price
        self._multiplicity = multiplicity
        self._initial_row = initial_row
        self._markup = markup
        self._delivery_time = delivery_time
        self._supplier_num = supp_num

    def get_vendor(self):
        return self._vendor

    def set_vendor(self, vendor):
        self._vendor = vendor

    def get_brand(self):
        return self._brand

    def get_name(self):
        return self._name

    def get_quantity(self):
        return self._quantity

    def get_price(self):
        return self._price

    def get_multiplicity(self):
        return self._multiplicity

    def get_initial_row(self):
        return self._initial_row

    def get_markup(self):
        return self._markup

    def get_delivery_time(self):
        return self._delivery_time

    def get_supplier_num(self):
        return self._supplier_num


test = Supplier("a", "s", "", "", "", "", "", "", "", "")
print(test.get_vendor())
