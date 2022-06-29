from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dinosaur1 = Dinosaur("Velociraptor", 5)
        dinosaur2 = Dinosaur("Dilophosaurus", 15)
        dinosaur3 = Dinosaur("T-Rex", 25)

        self.dinosaurs.append(dinosaur1)
        self.dinosaurs.append(dinosaur2)
        self.dinosaurs.append(dinosaur3)