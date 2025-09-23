# liste_notes = []
# nb_note = int(input("Combien de notes voulez-vous saisir ? "))

# for i in range(nb_note):
#     liste_notes.append(float(input("Nouvelle note: ")))

# print("La moyenne est de :", sum(liste_notes) / len(liste_notes))

continuer = "o"
liste_notes = []
note_max = int(input("Quelle est la note maximum de l'examen ? "))

while continuer == "o":
    note = float(input("Nouvelle note: "))
    while note < 0 or note > note_max :
        note = float(input(f"Veuillez corriger la note (entre 0 et {note_max}): "))

    liste_notes.append(note)
    continuer = input("Voulez-vous saisir une nouvelle note ? (o/n) ")

print("La moyenne est de :", round(sum(liste_notes) / len(liste_notes), 2))

