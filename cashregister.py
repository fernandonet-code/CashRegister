import variables as variable
import time
from os import *

class Customer():

    name = input("Name: ")
    id = int(input("ID: "))
    phone = int(input("Phone: "))
    direction = input("Direction: ")

    def __init__(self, name:str, id:int, phone:int, direction:str):
        self.name = name
        self.id = id
        self.phone = phone 
        self.direction = direction
    
    def showCustomer(self):        
        print("----------------------------------")
        print("Name: ", self.name)
        print("ID: ", str(self.id))
        print("Phone: ", str(self.phone))
        print("Direction: ", self.direction)
        print("----------------------------------")

class Product():

    id = int(input("ID: "))
    name = input("Name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    def __init__(self, id:int, name:str, price:float, quantity:int):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def showProduct(self):
        print("---------------------------")
        print("ID:    ", str(self.id))
        print("Name:  ", self.name)
        print("Price: ", str(self.price))
        print("Quantity: ", str(self.quantity))
        print("---------------------------")

class Bill():
    def __init__(self, customer:object):
        self.customer = customer
        self.listOfProducts = []
        self.totalCost = 0.0

    def addProduct(self, newProduct:object): # Add products to the bill
        self.listOfProducts.append(newProduct)
        print("Product added!")
    
    def removeProduct(self, id:int): # Remove a product and its associated quantity
        for i in range(0, len(self.listOfProducts)):
            if self.listOfProducts[i].id == id:
                self.listOfProducts.pop(i)
                print("Product removed!")
                break
    
    def showBill(self): # Show the bill
        Customer.showCustomer()
        print("ID","\t","Name","\t\t","Price","\t","Quantity")
        for i in range(len(self.listOfProducts)):             
            print(self.listOfProducts[i].id,"\t",
                  self.listOfProducts[i].name,"\t",
                  self.listOfProducts[i].price,"\t",
                  self.listOfProducts[i].quantity)

def createProduct():
    newProduct = Product()
    return newProduct

def createCustomer():
    newCustomer = Customer()
    return newCustomer

def createNewBill(customer:object):
    newBill = Bill(customer)
    return newBill

def deleteBill():
    global newBill
    del newBill

def showMainMenu():
    print("-----------------------------")
    print("|   1. Create new bill      |")
    print("|   2. Delete bill          |")
    print("|   3. Show bill            |")
    print("|   4. Pay                  |")
    print("-----------------------------")

def main():
    system('cls')
    showMainMenu()
    userOption = input(" Select an option: ")
    if userOption == "1":
        system('cls')
        variable.customer = createCustomer()
        print("-----------------------------")
        variable.newBill = createNewBill(variable.customer)
        variable.newBill.addProduct(createProduct())
        print("-----------------------------")  
        while True:
            userOption = input("Add another product? (y/n) ")
            print("-----------------------------")
            if userOption == "y" or userOption == "Y":
                variable.newBill.addProduct(createProduct())
                print("-----------------------------")
            else:
                break
    elif userOption == "2":
        del variable.newBill
    elif userOption == "3":
        system('cls')
        variable.newBill.showBill()   
    