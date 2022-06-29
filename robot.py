class Robot:

    name = ["Johnny 5", "Steve", "R2D2"]

    def __init__(self, name, Weapon): 
        self.name = name
        self.health = 100 
        self.attack_power = 150
        self.weapon = Weapon
        self.weapon_of_choice = ["Axe", "M4", "RPG"]

    
    def attack_dinosaur(self, dinosaur_to_attack):
        if self.attack_power > 10:
           self.attack_choice : int(input(f"Choose attack weapon: (1) {self.weapon_of_choice[0]}, (2) {self.weapon_of_choice[1]}, or (3) {self.weapon_choice[2]}"))
           return
        elif self.attack_choice == 1:
            print(f"{self.name} attacked {dinosaur_to_attack.type} with {self.weapon_choice[0]}")
            return
        elif self.attack_choice == 2:
            print(f"{self.name} attacked {dinosaur_to_attack.type} with {self.weapon_choice[1]}")
            return
        elif self.attack_choice == 3:
            print(f"{self.name} attacked {dinosaur_to_attack.type} with {self.weapon_choice[2]}")
            return

        self.attack_power -= 10
        dinosaur_to_attack.health -= self.weapon.attack_power
        print(f"{self.name} attack power is now {self.attack_power}")
        print(f"{dinosaur_to_attack.type} health is now {dinosaur_to_attack.health}")
