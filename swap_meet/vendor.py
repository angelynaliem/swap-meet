
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
#remove my item -> add to frend's inventory
#remove their item -> add to my inventory

# we call swap_items here
    # Wave 4
    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False

        my_first_item = self.inventory[0]
        friend_first_item = other_vendor.inventory[0]

        self.swap_items(other_vendor, my_first_item, friend_first_item)

        return True
#i remove my first item -> add to friend's inventory
#i remove friend's first item -> add to my inventory



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

# we call swap_items here
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

        if my_best_item is None or their_best_item is None:
            return False

        self.swap_items(other_vendor, my_best_item, their_best_item)

        return True

#enhancements 
    def swap_by_newest(self, other_vendor):
        #going through their inventory and my inventory to find newest item 
        # if age is less than the other item 
        
        # looping through my inventory and their inventory to find the newest item of each one
        # with the newest item from each inventory, we can call swap_items to swap the items
        my_newest_item = self.inventory[0]

        for item in self.inventory:
            if item.age < my_newest_item.age:
                my_newest_item = item

        their_newest_item = other_vendor.inventory[0]
        for item in other_vendor.inventory:
            if item.age < their_newest_item.age:
                their_newest_item = item

        self.swap_items(other_vendor, my_newest_item, their_newest_item)

        return True
