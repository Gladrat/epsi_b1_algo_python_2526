alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

mot = input("Votre mot (en minuscule): ")
decalage = int(input("Votre décalage: "))

code_secret = ""

for lettre in mot:
    pos = alphabet.index(lettre)

    print(f"Position de la lettre: {pos}")
    print(f"Décalage de la lettre: {pos + decalage}")

    if pos + decalage > 25:
        print(f"Résultat du décalage: {alphabet[pos + decalage - 26]}")
        code_secret = code_secret + alphabet[pos + decalage - 26]
    else:
        print(f"Résultat du décalage: {alphabet[pos + decalage]}")
        code_secret = code_secret + alphabet[pos + decalage]

print(f"Votre code secret: {code_secret}")