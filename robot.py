class Robot:
    def __init__(self): 
        self.name = "Johnny 5"
        self.attack_power = 25
        self.health = 50 

    def attack(self, dinosaur):
        dinosaur.health -= self.attack_power
        print(f"explain what happened")