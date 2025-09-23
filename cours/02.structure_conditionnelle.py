# SI

age = 5

# opérateurs de comparaisons

# <
# >
# ==
# <=
# >=
# !=

# if (age >= 18): # évalutation booléenne
#     print("Bienvenue au casino !")
#     print("Bienvenue au casino !")
#     print("Bienvenue au casino !")
#     print("Bienvenue au casino !")
#     # ICI
# else:
#     print("Accès interdit aux mineurs")
#     print("Accès interdit aux mineurs")
#     print("Accès interdit aux mineurs")
#     print("Accès interdit aux mineurs")
#     # ICI

# True == 1
# False == 0

# print(0 == ((False == 0) != True))

nb1 = 99
nb2 = 0

if (nb2 == 0):
    print("T'es nul, on peut pas diviser par 0")
else:
    print("Le résultat est " + str(nb1 / nb2))

# ------------------

if (nb2 != 0):
    print("Le résultat est " + str(nb1 / nb2))
else:
    print("T'es nul, on peut pas diviser par 0")

# -------------------

temperature = 22

# glace : <0
# liquide : 0 - 100
# vapeur : >100

# if (temperature <= 0):
#     print("C'est de la glace")
# if (temperature > 0 and temperature < 100):
#     print("C'est du liquide")
# if (temperature >= 100):
#     print("C'est de la vapeur")

if (temperature <= 0):
    print("C'est de la glace")
elif (temperature < 100):
    print("C'est du liquide")
else:
    print("C'est de la vapeur")