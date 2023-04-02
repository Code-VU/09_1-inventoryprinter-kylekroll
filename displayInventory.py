stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    
    x = None
    print("Inventory:")
    for item,value in inventory.items():
        if x is None:
            x = value
        else:
            x = x + value
        print(value, item)
    print("Total number of items:", x)



if __name__ == "__main__":
    displayInventory(stuff)
