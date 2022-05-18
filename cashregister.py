import time

class Product():
    def __init__(self, id:int, name:str, price:float, quantity:int):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def showProduct(self):
        print("---------------------------")
        print("id:    ", str(self.id))
        print("Name:  ", self.name)
        print("Price: ", str(self.price))
        print("Quantity: ", str(self.quantity))
        print("---------------------------")

class Bill():
    def __init__(self):
        self.listOfProducts = []
        self.quantities = []
        self.totalCost = 0.0

    def addProduct(self, newProduct:object, quantity:int): # Add products to the bill
        self.listOfProducts.append(newProduct)
        self.quantities.append(quantity)
        print("Product added!")
        time.sleep(2)
    
    def removeProduct(self, id:int): # Remove a product and its associated quantity
        for i in range(0, len(self.listOfProducts)):
            if self.listOfProducts[i].id == id:
                self.listOfProducts.pop(i)
                self.quantities.pop(i)
                print("Product removed!")
                time.sleep(2)
                break
    
    def showBill(self): # Show the bill
        for i in range(len(self.listOfProducts)):
            print("ID\tName\tPrice\tQuantity")
            print(self.listOfProducts[i].id,"\t",
                  self.listOfProducts[i].name,"\t",
                  self.listOfProducts[i].price,"\t",
                  self.listOfProducts[i].quantity)
        time.sleep(2)

def createProduct():
    id = int(input("id: "))
    name = input("Name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    newProduct = Product(id, name, price, quantity)
    return newProduct

def showMainMenu():
    print("-----------------------------")
    print("|   1. Create new bill      |")
    print("|   2. Delete bill          |")
    print("|   3. Show bill            |")
    print("|   4. Collect              |")
    print("-----------------------------")

def showSecondaryMenu():
    print("-----------------------------")
    print("|   1. Add new product      |")
    print("|   2. Remove product       |")
    print("-----------------------------")