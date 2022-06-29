
from herd import Herd
from fleet import Fleet
import random

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.team = self.select_team()
        self.battle_round()
        self.battle_details()
        
    def display_welcome(self):
        print("Welcome to grand battle of Robots vs Dinosaurs!Only one team shall win!")
        print("Each Robot and Dinosaur shall start with 100 health.")

    def select_team(self):
        select_team = int(input("Select your team: (1) Robots (2) Dinosaurs  "))
        if select_team == 1:
            print("You have chosen the fleet of Robots.")
            return select_team
        elif select_team == 2:
            print("You have chose the herd of Dinosaurs.")
            return select_team
        else:
            print("Not a valid option. Try again.")
            self.select_team()

    def battle_round(self):
        first_round = random.randint(1,2)
        if first_round == 1:
            print("Robots go first!")
            first_round == 1
            return first_round
        if first_round == 2:
            print("Dinosaurs go first.")
            first_round = 2
            return first_round

    def battle_details(self):         
        #if first_round == 1:
            while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0:
                if self.fleet.robots[0].health > 0:
                    self.robot_turn()
                    if self.herd.dinosaurs[0].health <= 0:
                        print(f"{self.herd.dinosaurs[0].type} is finished.")
                        self.herd.dinosaurs.remove(self.fleet.robots[0])
                    elif self.fleet.robots[0].health <= 0:
                        print(f"{self.fleet.robots[0].name} is finished.")
                        self.fleet.robots.remove(self.fleet.robots[0])

                    if len(self.fleet.robots) == 0:
                        self.display_winners_dinosaurs()
                        return
                    elif len(self.herd.dinosaurs) == 0:
                        self.display_winners_robot()
                        return

    def dinosaur_turn(self):
        self.show_dinosaur_opponent_options()
        self.herd.dinosaurs[0].attack_robot(self.fleet.robots[0])
        self.dinosaurs_turn()
        self.robot_turn()

        if self.herd.dinosaurs[0].health <= 0:
            print(f"{self.herd.dinosaurs[0].type} is finished")
            self.herd.dinosaurs.remove(self.herd.dinosaurs[0])
        elif self.fleet.robots[0].health <= 0:
            print(f"{self.fleet.robots[0].name} is finished")
            self.fleet.robots.remove(self.fleet.robots[0])
        if len(self.fleet.robots) == 0:
            self.display_winners_dinosaurs()
        elif len(self.herd.dinosaurs == 0):
            self.display_winners_robots()
            return

        self.robot_turn()
        if self.herd.dinosaurs[0].health <= 0:
            print(f"{self.herd.dinosaurs[0].type} is finished.")
            self.herd.dinosaurs.remove(self.herd.dinosaurs[0]) 
        elif self.fleet.robots[0].health <= 0:
            print(f"{self.fleet.robots[0].name} is finished.") 
            self.fleet.robots.remove(self.fleet.robots[0]) 
        if len(self.fleet.robots) == 0:
            self.diplay_winners__dinosaurs()  
        elif len(self.herd.dinosaurs) == 0:
            self.display_winners_robots()
            return  

    def robot_turn(self):
        self.show_robot_opponent_options()
        self.fleet.robots[0].attack_dinosaur(self.herd.dinosaurs[0])

    def show_dinosaur_opponent_options(self):
        sub = 1
        for segment in self.fleet.robots:
            print(f"{segment.name} has {segment.health} health.")
            sub += 1
            
    def show_robot_opponent_options(self):
        sub = 1
        for segment in self.herd.dinosaurs:
            print(f"{segment.name} has {segment.health} health.")
            sub += 1
           
    def display_winners_robot(self):
        if self.team == 1:
            print("The Robot fleet has conquered the herd of Dinosaurs. Congrats on the win!")
        if self.team == 2:
            print("The Robot fleet has conquered the herd of Dinosaurs. Sorry you have lost!")
            
    def display_winners_dinosaurs(self):
        if self.team == 2:
            print("The herd of Dinosaurs has conquered the fleet of Robots. Congrats n the win!")
        if self.team == 1:
            print("the herd of Dinosaurs has conquered the fleet of Robots. Sorry you have lost!")
