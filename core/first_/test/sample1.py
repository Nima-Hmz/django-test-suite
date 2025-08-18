class Car:
    def __init__(self, name) -> None:
        self.name = name 
        self.health = True
        self.need_repair = False

    def move(self):
        return f"the {self.name} can move"

    def car_health(self):
        return self.health
    
    def car_need_rapair(self):
        return self.need_repair
    
    def car_error(self):
        raise ValueError
    


