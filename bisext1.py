# -*-coding:Latin-1 -*
import os # On importe le module os 

# Programme testant si une année, saisie par l'utilisateur, est bissextile ou non
try: # On essaye de convertir l'année en entier
    annee = input("Saisissez une année : ") # On attend que l'utilisateur saisisse l'année qu'il désire tester
    annee = int(annee) # Risque d'erreur si l'utilisateur n'a pas saisi un nombre

    if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
        print("L'année saisie est bissextile.")
    else:
        print("L'année saisie n'est pas bissextile.")
except ValueError:
    print("Vous n'avez pas saisi un nombre.")
finally:
    annee = input("Saisissez une année : ") # On attend que l'utilisateur saisisse l'année qu'il dÃ©sire tester
    annee = int(annee) # Risque d'erreur si l'utilisateur n'a pas saisi un nombre

    if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
        print("L'année saisie est bissextile.")
    else:
        print("L'année saisie n'est pas bissextile.")
os.system("pause")
