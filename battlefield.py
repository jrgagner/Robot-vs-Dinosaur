
from dinosaur import Dinosaur
from robot import Robot
import random

class Battlefield:
    def __init__(self):
        self.robot = Robot()
        self.dinosaur = Dinosaur()

    def run_game(self):
        self.display_welcome()
        self.team = self.choose_team()
        self.battle()
        
    def display_welcome(self):
        print("\nWelcome to grand battle of Robots vs Dinosaurs!\nOnly one team shall win!\n")
        print("Each Robot and Dinosaur shall start with 100 health.")

    def battle_phase(self):
        self.dinosaur.attack(self.robot)
        if self.dinosaur.health >= 0:
            print(f"Dinosaur is not dead!")
            return self.dinosaur.attack    
        elif self.robot.health >= 0:
            print(f"Robot is not dead!")
            return self.robot.attack

    def select_team(self):
        select_team = int(input("Select your team: (1) Robots (2) Dinosaurs"))
        if select_team == 1:
            print("You have chosen the fleet of Robots.")
            return select_team
        elif select_team == 2:
            print("You have chose the herd of Dinosaurs.")
            return select_team
        else:
            print("Not a valid option. Try again.")
            self.select_team()

    def battle(self):
        first_round = random.randint(1,2)
        if first_round == 1:
            print("Robots go first!")
            first_round == 1
        if first_round == 2:
            print("Dinosaurs go first.")
            first_round = 2
        