while True:
    print("""1. Eau
2. Jus
3. Soda
4. Thé
5. Quitter""")

    choix = int(input("Votre choix: "))

    liste_boissons = ["Eau", "Jus", "Soda", "Thé"]

    if choix - 1 >= 1 and choix - 1 <= 3:
        print(f"Vous avez choisi {liste_boissons[choix - 1]}")
    elif choix - 1 == 4:
        exit()
    else:
        print("Choix invalide")