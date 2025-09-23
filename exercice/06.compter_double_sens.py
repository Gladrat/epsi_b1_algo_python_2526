# Partir d'un nombre entier x = 10
# Afficher 10 fois : 

    # Le premier nombre suivant (11)
    # Le premier nombre précédent (9)

    # Le second nombre suivant (12)
    # Le second nombre précédent (8)

    # [...]

    # Jusqu'au dixième nombre suivant (??)
    # Dixième nombre précédent (??)




# Contrainte :  n'utiliser qu'une seule boucle (POUR)

x = 10
for i in range(1, x + 1):
    print(x + i)
    print(x - i)
    print("---")

# for i in range(x):
#     break

# print(11)
# print(9)
# print(12)
# print(8)