def kontrolli_parooli_pikkust(parool):
    # Määrame parooli minimaalse lubatud pikkuse
    minimaalne_pikkus = 8

    # Kontrollime, kas parool on piisavalt pikk
    if len(parool) >= minimaalne_pikkus:
        return True  # Parooli pikkus on sobiv
    else:
        return False  # Parool on liiga lühike

# Näide funktsiooni kasutamisest
parool = input("Sisesta parool: ")

if kontrolli_parooli_pikkust(parool):
    print("Parooli pikkus on sobiv.")
else:
    print("Viga! Parool peab olema vähemalt 8 märki pikk.")