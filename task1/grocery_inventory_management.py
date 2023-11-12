import time
inventory={'TOMATO':12}
def addItem():
    i,qty=0,0
    i=input("enter the product name:")
    i=i.upper()
    if i in inventory.keys():
        print("***PRODUCT EXISTS***")
        return
    qty=int(input(f'enter quantity of {i} :'))
    inventory.setdefault(i,qty)
    print(i,"\n***ADDED SUCCESSFULLY***\n----------------------------\n")

def updateInv(item:str):
    if item not in inventory:
        print("***INVALID PRODUCT OR PRODUCT NOT FOUND***\n-----------------------------------")
        return
    qty=int(input(f'Enter new quantity of {item} : '))
    inventory[item]=qty
    print(f'***{item} SUCCESSFULLY UPDATED***\n-----------------------------------')

def viewInv():
    if not inventory:
        print("\n***EMPTY INVENTORY***\n")
        return
    for i in inventory:
        print(f'{i} :: {inventory[i]}')
    print("\n-------------------\n")

def delItem(item:str):
    if item not in inventory:
        print("***INVALID PRODUCT OR PRODUCT NOT FOUND***\n-----------------------------------")
        return
    print(f'***{item} DELETED SUCCESSFULLY***')
    del inventory[item]

def menu():
    while(True):
        print("SELECT AN OPTION")
        print("1.Add new Items\n2.Update inventory\n3.View Inventory\n4.Remove Items\n5.Exit")
        print("----------------\nSelect and option --> ")
        choice=int(input())
        if choice==1:
            addItem()
        elif choice==2:
            itmN=input("Enter Product to be updated: ")
            itmN=itmN.upper()
            updateInv(itmN)
        elif choice==3:
            viewInv()
        elif choice==4:
            itmName=input("Enter Product to be deleted: ")
            itmName=itmName.upper()
            delItem(itmName)
        elif choice==5:
            time.sleep(1)
            print('***THANK YOU!***')
            exit(0)
        else:
            print("***INVALID INPUT***")
menu()