import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

futur_ex = input("Quel est le prénom ciblé ? ")
res = 0

for lettre in futur_ex:
    res = res + alphabet.index(lettre) + 1

print(f"l'ex: {res}")

res = res % 10
print(f"Indice de rupture: {res}")

liste_raisons = ["tu as insisté pour nommer notre futur chien 'Monsieur Patate'",
                 "je ne peux pas rester avec quelqu'un qui ne sait pas plier une serviette",
                 "ton père est fan de Jean-Marie Bigard et passe son temps à l'imiter"]
liste_circonstances = ["pendant un repas de famille",
                       "le jour de mon anniversaire",
                       "à la messe"]
liste_actions = ["j'ai crush sur le vendeur de poisson",
                 "j'ai réalisé que nos signes astro sont incompatibles",
                 "j'ai décidé de devenir un pirate et de naviguer les sept mers"]

liste_humour = [", au fait j'ai jamais aimé tes parents", "HUMOUR 2"]

print(liste_humour)

print(f"{random.choice(liste_raisons)} {random.choice(liste_circonstances)} et {random.choice(liste_actions)}{"" if res != 9 else random.choice(liste_humour)}.")