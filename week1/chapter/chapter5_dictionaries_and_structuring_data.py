# # inventory.py
# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#
#
# def displayInventory(inventory):
#     print("Inventory:")
#     item_total = 0
#     for k, v in inventory.items():
#         print(str(v) + "  " + k)
#         item_total += v
#     print("Total number of items: " + str(item_total))
#
#
# displayInventory(stuff)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}
def addToInventory(inventory, addedItems):
    # write code here
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        item_total += count
    print(f"Total number of items: {item_total}")

inventory = addToInventory(inv, dragonLoot)
displayInventory(inventory)
