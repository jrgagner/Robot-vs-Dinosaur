from weapon import Weapon
from robot import Robot

class Dinosaur:
    def __init__(self):
        self.name = "Steve"
        self.attack_power = 25
        self.health = 50

    def attack(self, robot):
        robot.self.health -= self.attack_power
        print(f"Dinosaur Steve has attacked Robot Johnny 5 with a axe")
        

    