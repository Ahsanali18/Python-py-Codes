class Animal:
    def __init__(self, name):
        self.name=name

    def eat(self):
        print(f"Animal {self.name} is eating")

    def sleep(self):
        print(f"Animal {self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"Animal {self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"Animal {self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()
# rabbit.hunt()
rabbit.eat()
rabbit.sleep()

# hawk.flee()
hawk.hunt()
hawk.eat()
hawk.sleep()

fish.flee()
fish.hunt()
fish.eat()
fish.sleep()