
class animal(object):
    
    def __init__(self, numberOfLegs, color, presenceOfFur, weight, length, species, name):
        self.numberOfLegs = numberOfLegs
        self.color = color
        self.presenceOfFur = presenceOfFur
        self.weight = weight
        self.length = length
        self.species = species
        self.name = name
        
    def getName(self):
        return self.name
    
    def getSpecies(self):
        return self.species
    
    def __str__(self):
        return "%s is a %s" % (self.name, self.species)

    def sleep(self):
        return "%s the %s is sleeping." % (self.name, self.species)
        
    def breathe(self):
        return "%s the %s is breathing." % (self.name, self.species)
        
    def walk(self):
        return "%s the %s is walking." % (self.name, self.species)


myPet1 = animal(4, "brown", "true", 24, 36, "canine", "Roofus")

print(myPet1)

print(myPet1.sleep())

print(myPet1.breathe())

print(myPet1.walk())

print("########################################")

myPet2 = animal(4, "grey", "true", 7, 27, "feline", "Mischief")

print(myPet2)

print(myPet2.sleep())

print(myPet2.breathe())

print(myPet2.walk())