
userName = ["Jazelle","Triszha", "Jholia"]
password = ["123", "456", "789"]

currentName = input("Enter username: ")
currentPass = input("Enter password: ")

for account in range(len(userName)):
    if currentName == userName[account] and currentPass == password[account]:
        print("Welcome " +userName[account]+ "!")
        break
else:
    print("Account not found!")



