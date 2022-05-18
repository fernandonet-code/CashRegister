from cashregister import *
from os import *

listOfProducts = []

while(True):
    system("cls")
    showMainMenu()

    userOption = input("    Select an option: ")

    if userOption == "1": # Create new bill
        system("cls")
        newBill = Bill()
        system("cls")
        showSecondaryMenu()
        userOption = input("    Select an option: ")
        if userOption == "1": #Add new product
            system("cls")
            newProduct = createProduct()
            newBill.addProduct(newProduct, newProduct.quantity)
        elif userOption == "2": # Remove product
            id = int(input("Id to remove?: "))
            newBill.removeProduct(id)
    elif userOption == "2": # Delete bill
        newBill = None
        print('Bill deleted!')
        time.sleep(1)
    elif userOption == "3": # Show bill
        if newBill == None:
            print("A bill has not been created yet")
            time.sleep(1)
        else:
            newBill.showBill()
    elif userOption == "4": # Collect
        pass
