#Creating class
class Character:
    #Attribute-default value
    name = "Jazelle"
    hp = 100
    mp = 50
    atk = 15
    lvl = 2

#Creating object
characterOne = Character()
characterTwo = Character()

#Access attribute
print("Character 1")
print(characterOne.name)
characterOne.name = "Ejhie"
print(characterOne.name)
characterOne.hp = 200
print(characterOne.hp)

print("\nCharacter 2")
characterTwo.name = "Jholia"
print(characterTwo.name)
characterTwo.hp = 300
print(characterTwo.hp)

class Product:
    id = 1000
    name = "cutie"
    qty = 30

productOne = Product()

print("\nProduct One")
print(productOne.id)
print(productOne.name)
print(productOne.qty)

