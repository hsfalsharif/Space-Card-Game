class Card:
    
    def __init__(self, fuel, mass, desc, effect):
        self.fuel = fuel
        self.mass = mass
        self.desc = desc
        self.effect = effect

    def execute_effect(self):
        self.effect()
