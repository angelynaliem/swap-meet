import uuid


class Item:
    def __init__(self, id=None, condition=0):
        if id is not None:
            self.id = id
        else:
            self.id = uuid.uuid4().int  

        self.condition = condition 

    #special __str__ method 
    def __str__(self):
        return (f"An object of type Item with id {self.id}.")
        
    def get_category(self):
        name_of_class = "Item"
        return name_of_class

    def condition_description(self):
        if self.condition == 0:
            return (f"It's time to let go!")
        elif self.condition == 1:
            return (f"This might be the last time to use it")
        elif self.condition == 2:
            return (f"It's tearing apart")
        elif self.condition == 3:
            return (f"It's still good!")
        elif self.condition == 4:
            return (f"Very good condition")
        elif self.condition == 5:
            return (f"Mint condition")

