class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} barks.")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def meow(self):
        print(f"{self.name} meows.")

class PetOwner:
    def __init__(self, name, pets):
        self.name = name
        self.pets = pets

    def __str__(self) -> str:
        return f"owner name : {self.name}, has pets : {self.pets}"

    def walk_pets(self):
        for pet in self.pets:
            print(f"{self.name} is walking {pet.name}.")

class PtOwnrClub:
    def __init__(self, pet_owners) -> None:
        self.pet_owners = pet_owners
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.pet_owners): 
            item = self.pet_owners[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration
        
    def __str__(self) -> str:
        output_str = ""
        for each_owner in self.pet_owners:
            output_str += str(each_owner) + " "
        return output_str

# Creating instances
budy_dog = Dog("Buddy", "Golden Retriever")
wh_cat = Cat("Whiskers", "Tabby")

bad_dog = Dog("Bad Man Dog", "Devil Dog")
whiny_cat = Cat("Chintan", "Screamy White")

pet_owner = PetOwner("John", [budy_dog, wh_cat])
pet_owner_2 = PetOwner("Tenalij Rama", [bad_dog, whiny_cat])

# Demonstrating inheritance and composition
budy_dog.bark()  # Inherited from Dog
wh_cat.meow()  # Inherited from Cat
pet_owner.walk_pets()  # Composition of PetOwner and multiple pets

pet_owner_club_ludh = PtOwnrClub([pet_owner, pet_owner_2])
print(pet_owner_club_ludh)

