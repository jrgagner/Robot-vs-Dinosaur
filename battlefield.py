
from dinosaur import Dinosaur
from robot import Robot 

class Battlefield:
    def __init__(self):
        self.robot = Robot()
        self.dinosaur = Dinosaur()

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        
    def display_welcome(self):
        print("Welcome to grand battle for the times! Only one shall win!")
    
    def battle_phase(self):
        self.dinosaur.attack(self.robot)
        if self.dinosaur.health >= 0:
            print(f"Dinosaur is not dead!")
            return self.dinosaur.attack    
        elif self.robot.health >= 0:
            print(f"Robot is not dead!")
            return self.robot.attack

champion = [Robot, Dinosaur]
winner_declared = champion

def display_winner(self):
        self.battle_phase()
        if self.robot == 0:
            print(f"Dinosaur is the winner!")
            return winner_declared
        elif self.dinosaur == 0:
            print(f"Robot is the winner!")
            return winner_declared

#print(f"Explain what happen in the battle and who won.")
