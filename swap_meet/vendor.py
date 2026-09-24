
class Vendor:

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

    # Wave 2
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item

    # Wave 3
    def swap_items(self, other_vendor, my_item, their_item):
        
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        # Removes my item from my inventory, adds to friend's inventory
        self.remove(my_item)

        other_vendor.inventory.append(my_item)
    
        # Removes their item from friend's inventory and adds to my inventory
        other_vendor.remove(their_item)
    
        self.add(their_item)

        return True

    # Wave 4
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])

    # Wave 6
    def get_by_category(self, category):
        category_inventory = []
        
        for item in self.inventory:
            if category == item.get_category():
                category_inventory.append(item)

        return category_inventory

    def get_best_by_category(self, category):

        initial_condition = 0
        highest_condition_item = None
        
        for item in self.inventory:

            if category == item.get_category():

                if item.condition > initial_condition:
                    initial_condition = item.condition
                    highest_condition_item = item
        
        return highest_condition_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):

        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item:
            return False

        return self.swap_items(other_vendor, my_best_item, their_best_item)