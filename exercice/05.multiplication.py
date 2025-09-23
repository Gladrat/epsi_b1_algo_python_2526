# Demander à l'utilisateur de saisir 2 nombres entiers positifs
# Multiplier ces deux nombres sans utiliser l'opérateur de multiplication
    
# Exemple : (6 * 7) == (6 + 6 + 6 + 6 + 6 + 6 + 6) == 42

# Afficher : "Le produit de nombre_1 * nombre_2 est de ..."

x = 458
y = 9999
res = 0

while y != 0:
    res = res + x
    y = y - 1

print(res)

x = 6
y = 7
res = 0
for _ in range(y):
    res += x
print(res)