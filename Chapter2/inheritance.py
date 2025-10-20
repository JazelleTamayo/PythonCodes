from os import system
system('cls')

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")


    def speak(self):
        print("I don't know what to say")
        
        
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old, with color {self.color} fur.")


    def speak(self):
        print("Meow")
        
class Dog(Pet): 
    def speak(self):
        print("Bark")
        
      
class Fish(Pet):
    pass
        
def main():
    p = Pet("Tim", 19)
    p.show()
    p.speak()
    
    c = Cat("Bill", 12, "Brown")
    c.speak()
    c.show()
    
    d = Dog("Jil", 25)
    d.speak()
    d.show()
    
    f = Fish("Ben", 10)
    f.speak()
         
     
if __name__ == "__main__":
    main()