def savePassToTxt(passWrd):
    try:
        with open("passwords.txt", "a") as file:
            file.write(passWrd+";")
    except FileNotFoundError:
        open("passwords.txt", "x")
        savePassToTxt(passWrd)


def checkUsedPasswords(num, passWrd):
    try:
        with open("passwords.txt", "r") as file:
            passwords = file.read().split(";")
            for idx in range(num):
                if passWrd == passwords[-idx]:
                    print("already used")
                    return 1
                
    except FileNotFoundError:
        return 0

