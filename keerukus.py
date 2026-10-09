def check_difficulty(parool):
    suurtaht = any(t.isupper() for t in parool)
    
    vaiketaht = any(t.islower() for t in parool)
    
    number = any(t.isdigit() for t in parool)
    
    erimark = any(not t.isalnum() and not t.isspace() for t in parool)
    
    return suurtaht and vaiketaht and number and erimark

parool = input("Sisesta Parool: ")

if check_difficulty(parool):
    print("Parool vastab nõuetele")
else:
    print("Parool ei vasta nõuetele")
