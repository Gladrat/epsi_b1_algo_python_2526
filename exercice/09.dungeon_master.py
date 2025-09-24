import random

def generer_niveau():
    niveau = []
    for i in range(20):
        niveau.append(random.randint(0, 1))
    # print(niveau)
    return niveau


un_niveau = generer_niveau()
print(un_niveau)