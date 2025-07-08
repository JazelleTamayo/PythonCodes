#Nested for Loop
for x in range(2):
    for y in range(2):
        print("*")


print("*",end="")
print("*")

for do in range(5):
    for hi in range(5):
        print("*",end="")
    print()

#Readin Multi-dimensional collections using nested for loop

courseStudents = [
    ["BSIT", "David"],
    ["BSIT", "Alenere"],
    ["BSCS", "Patrick"],
    ["BSCS", "Jaymar"],
    ["BSCS", "Emman"]
]

print(courseStudents[0][1])

for info in courseStudents:
    for i in info:
        print(i)
    print()

