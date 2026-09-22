import uuid

class Electronics:
    def __init__(self, id=None, type="Unknown"):
        if id is not None:
            self.id = id
        else:
            self.id = uuid.uuid4().int   

        self.type = type

    def get_category(self):
        return "Electronics"

    def __str__(self):
        return (f"An object of type Electronics with id {self.id}. This is a {self.type} device.")

    
