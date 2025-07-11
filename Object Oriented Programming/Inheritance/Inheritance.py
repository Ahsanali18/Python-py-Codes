class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")


class Mouse(Animal):
    def speak(self):
        print("SQUEEK")


puppy_dog = Dog("Scobby")
kitty_cat = Cat("Tom")
micky_mouse = Mouse("Micky") 

print(micky_mouse.name)
print(micky_mouse.is_alive)
micky_mouse.eat()
micky_mouse.sleep()

puppy_dog.speak()
kitty_cat.speak()
micky_mouse.speak()