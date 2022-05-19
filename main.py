from cashregister import *
from os import *

if __name__ == '__main__':
    while True:
        newCustomer = Customer("Fernando Alvarez", 1121905220, 3214053875, "Calle 4E # 20 - 33")
        newBill = Bill(newCustomer)
        newProduct = Product(1, "Televisor", 2100, 1)
        newProduct2 = Product(2, "Nevera", 2500, 1)
        newProduct3 = Product(3, "Plancha", 200, 2)
        newBill.addProduct(newProduct)
        newBill.addProduct(newProduct2)
        newBill.addProduct(newProduct3)
        newBill.showBill()
        newBill.removeProduct(2)
        newBill.showBill()
        input(" ")