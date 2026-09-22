
class Vendor:

#Each `Vendor` will have an attribute named `inventory`, 
#which is an empty list by default

#When we instantiate an instance of `Vendor`, we can 
#optionally pass in a list with the keyword argument `inventory`

    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return None
        self.inventory.remove(item)
        return item

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
            