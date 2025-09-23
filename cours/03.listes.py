# Déclarations

liste_eleves = ["John", "Lisa", "Arnaud", "Eric", "Philomée"]


# Affichage de listes


# print(liste_notes[0])
# print(liste_notes[1])
# print(liste_notes[2])
# print(liste_notes[3])
# print(liste_notes[4])

# print(liste_notes[-1])
# print(liste_notes[-2])
# print(liste_notes[-3])
# print(liste_notes[-4])
# print(liste_notes[-5])


# Manipulations de listes

liste_notes = [14.0, 13.5, 12.0, 19.0, 17.5]
print(liste_notes)

liste_notes.append(2.5)
print(liste_notes)
deleted_value = liste_notes.pop(0)
print("La valeur supprimée:", deleted_value)

liste_notes.reverse()

print(liste_notes)