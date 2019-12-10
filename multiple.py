# -*-coding:Latin-1 -*
import os # On importe le module os
nb=input("saisissez un nombre : ")
nb=int(nb)
i = 0 # C'est notre variable compteur que nous allons incrémenter dans la boucle

while i < 100: # Tant que i est strictement inférieure à 10
    print(i + 1, "*", nb, "=", (i + 1) * nb)
    i += 1 # On incrémente i de 1 à chaque tour de boucle
os.system("pause")