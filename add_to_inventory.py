## add_to_inventory.py

def displayInventory(stuff):
    print("Inventory:")
    item_total = 0
    for k, v in stuff.items():
         vv = str(v)
         print(vv + ' ' + k)
         item_total = item_total + v
    print("Total number of items: " + str(item_total))


def addToInventory(stuff):
    for k in dragonLoot:
        if k not in stuff:
            stuff[k] = 1
        else:
            stuff[k] += 1


stuff = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(stuff)
displayInventory(stuff)

