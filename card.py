class Card:
    
    def __init__(self,name, effect):
        self.name = name
        self.effect = effect

    def execute_effect(self):
        self.effect()
