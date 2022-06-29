class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power
        self.attack_type = ('Claw', 'Knife', 'Bite & Shred')

        name = ("Velociraptor", "Dilophosaurus", "T-Rex")

    def attack_robot(self, robot_to_attack):
        if self.attack_power > 10:
           self.attack_choice = int(input(f'Choose attack type: (1) {self.attack_type[0]}, (2) {self.attack_type[1]}, or (3) {self.attack_type[2]}.'))
           return               
        elif self.attack_choice == 1:
            print(f'{self.attack_type} attacked {robot_to_attack.name} with {self.attack_type[0]}')
            return
        elif self.attack_choice == 2:
            print(f'{self.attack_type} attacked {robot_to_attack.name} with {self.attack_type[1]}')
            return
        elif self.attack_choice == 3:
            print(f'{self.attack_type} attacked {robot_to_attack.name} with {self.attack_type[2]}')
            return

        self.energy -= 10
        robot_to_attack.health -= self.attack_power
        print(f'{self.type_weapon} energy is now {self.energy}')
        print(f'{robot_to_attack.name} health is now {robot_to_attack.health}')
