#Object Oriented Programming in Python
from os import system
system('cls')



class Pet:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("\nPet Created")
        
    def meow(self, x):
        print(f"I am {self.name} the {self.breed} cat!")
        return x + 1
        
    def bark(self):
        print(f"I am {self.name} the {self.breed} dog!")
        print("arfff")

    def get_name(self):
        return self.name
        
    def get_breed(self):
        return self.breed
    
    
def main():
    dog1 = Pet("brown", "poddle")
    dog1.bark()
    print(dog1.name)

    cat1 = Pet("Lucky", "Persian")
    print(f"My age is {cat1.meow(4)}.")
    
    dog2 = Pet("Happy", "Chihua-hua")
    print(dog2.get_name())
    
    cat2 = Pet("Pluff", "Foldex")
    print(cat2.get_breed())
    
	
if __name__ == "__main__":
    main()