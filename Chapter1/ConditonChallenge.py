grade1 = int(input("DIGILOG: "))
grade2 = int(input("APPSDEV: "))
grade3 = int(input("DATACOM: "))

average = (grade1 + grade2 + grade3) / 3

if average > 100 or average <= 50:
    print("InvaliD Grade")
elif average >= 98:
    print("With Highest Honors")
elif average >= 95:
    print("With High Honor")
elif average >= 90:
    print("With Honors")
elif average >= 75:
    print("Passed")
else:
    print("Failed")



