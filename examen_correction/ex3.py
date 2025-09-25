import random # 1

nombre_secret = random.randint(1, 10) # 2

trouve = False

while trouve == False: # 3 4
    essai = int(input("Devine le nombre entre 1 et 10 : ")) # 5
    if essai > nombre_secret:
        print("Trop grand !")
    elif essai < nombre_secret: # 6
        print("Trop petit !") # 7
    else:
        print("Bravo, tu as trouvé !")
        trouve = True # 8