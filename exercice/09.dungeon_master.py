import random

def generer_niveau():
    niveau = []
    for i in range(20):
        niveau.append(random.randint(0, 1))
    return niveau

gagne = False
nb_partie = 0

while gagne == False:
    nb_partie = nb_partie + 1
    niveau = generer_niveau()
    print(niveau)
    vie = 1
    for salle in niveau:
        if salle == 0:
            print("Salle vide")
        elif salle == 1:
            print("Combat")

            des = random.randint(1, 6)
            if des <= 3:
                vie = vie - 1
                print(f"Une vie perdue ! (Il en reste {vie})")

        if vie <= 0:
            print("JEU PERDU !")
    
    if vie > 0:
        gagne = True

print("JEU GAGNE !")
print(f"Vous avez fait : {nb_partie} parties")