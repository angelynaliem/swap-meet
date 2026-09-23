
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
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False

        my_first_item = self.inventory[0]
        friend_first_item = other_vendor.inventory[0]

        self.inventory.remove(my_first_item)
        other_vendor.inventory.append(my_first_item)


        other_vendor.inventory.remove(friend_first_item)
        self.inventory.append(friend_first_item)

        return True

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

        if other_vendor.inventory == []:
            return False
        
        if self.inventory == []:
            return False

        my_items_category = []
        for item in self.inventory:
            my_items_category.append(item.get_category())

        if their_priority not in my_items_category:
            return False

        their_items_category = []
        for item in other_vendor.inventory:
            their_items_category.append(item.get_category())

        if my_priority not in their_items_category:
            return False 

        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        other_vendor.inventory.remove(their_best_item)
        self.inventory.remove(my_best_item)

        other_vendor.inventory.append(my_best_item)
        self.inventory.append(their_best_item)

        return True

                    
        