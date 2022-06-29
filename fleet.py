from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        weapon1 = Weapon("Axe", 5)
        weapon2 = Weapon("M4", 15)
        weapon3 = Weapon("RPG", 25)

        robot1 = Robot("Johnny 5", weapon1)
        robot2 = Robot("Steve", weapon2)
        robot3 = Robot("R2D2", weapon3)

        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)
        
