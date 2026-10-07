# import uuid
from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, fabric="Unknown", condition=0, age=0):
        super().__init__(id, condition, age)

        self.fabric = fabric
    
    def get_category(self):
        return "Clothing"

    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str} It is made from {self.fabric} fabric.")

    