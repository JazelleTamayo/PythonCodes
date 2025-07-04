
print("Who is the father of classical mechanics?")

i = 0
while i < 3:
    answer = input("Answer: ")
    if answer == "Isaac Newton":
        print("You are correct!")
        break
    elif i < 2:
        print("Please try again")
        i += 1
    else:
        print("You already used your 3 chances!")

