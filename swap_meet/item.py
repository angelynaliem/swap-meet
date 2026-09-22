import uuid


class Item:
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.id = uuid.uuid4().int       
        
    def get_category(self):
        name_of_class = "Item"
        return name_of_class