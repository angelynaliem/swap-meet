import uuid


class Item:
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.id = uuid.uuid4().int   

    #special __str__ method 
    def __str__(self):
        return (f"An object of type Item with id {self.id}.")
        
    def get_category(self):
        name_of_class = "Item"
        return name_of_class

