

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
    #print statement of what will happen

    def battle_phase(self):
        self.dinosaur.attack(self.robot)
        pass
# while loop


    def display_winner(self):
        pass
    #explain what happened during the battle