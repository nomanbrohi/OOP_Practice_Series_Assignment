class Product():
    def __init__(self,price):
        self.__price = price # private variable

    @property               # Decorator to access the private variable
    def price(self):
        return self.__price

    @price.setter           # Decorator to update the value
    def price(self,value):
        self.__price = value

    @price.deleter          # Decorator to delete the value
    def price(self):
        del self.__price

p = Product(52)
print(p.price)
p.price = 100
print(p.price)
p.price = 500
del p.price
print(p.price)