#Self Parameter
class Character:
    def __init__(self, name, hp, mp, atk, lvl):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.lvl = lvl
        print("Created " +self.name)

#Constructor
charOne = Character("Jazelle", 500, 100, 50, 45 )
print(charOne.name)
print(charOne.hp)
charTwo = Character("Ejhie", 450, 130, 65, 50)
print(charTwo.name)
print(charTwo.hp)


