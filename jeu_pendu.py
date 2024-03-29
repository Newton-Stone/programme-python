# -*-coding:Latin-1 -*
import os # On importe le module os 

"""Ce fichier contient le jeu du pendu.

Il s'appuie sur les fichiers :
- donnees_pendu.py
- fonctions_pendu.py"""


from donnees_pendu import *
from fonctions_pendu import *

# On r�cup�re les scores de la partie
scores = recup_scores()

# On r�cup�re un nom d'utilisateur
utilisateur = recup_nom_utilisateur()

# Si l'utilisateur n'a pas encore de score, on l'ajoute
if utilisateur not in scores.keys():
    scores[utilisateur] = 0 # 0 point pour commencer

# Notre variable pour savoir quand arr�ter la partie
continuer_partie = 'o'

while continuer_partie != 'n':
    print("Joueur {0}: {1} point(s)".format(utilisateur, scores[utilisateur]))
    mot_a_trouver = choisir_mot()
    lettres_trouvees = []
    mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)
    nb_chances = nb_coups
    while mot_a_trouver!=mot_trouve and nb_chances>0:
        print("Mot � trouver {0} (encore {1} chances)".format(mot_trouve, nb_chances))
        lettre = recup_lettre()
        if lettre in lettres_trouvees: # La lettre a d�j� �t� choisie
            print("Vous avez d�j� choisi cette lettre.")
        elif lettre in mot_a_trouver: # La lettre est dans le mot �trouver
            lettres_trouvees.append(lettre)
            print("Bien jou�.")
        else:
            nb_chances -= 1
            print("... non, cette lettre ne se trouve pas dans le mot...")
        mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)

    # A-t-on trouv� le mot ou nos chances sont-elles �puis�es ?
    if mot_a_trouver==mot_trouve:
        print("F�licitations ! Vous avez trouv� le mot {0}.".format(mot_a_trouver))
    else:
        print("PENDU !!! Vous avez perdu.")

    # On met � jour le score de l'utilisateur
    scores[utilisateur] += nb_chances

    continuer_partie = input("Souhaitez-vous continuer la partie (O/N) ?")
    continuer_partie = continuer_partie.lower()

# La partie est finie, on enregistre les scores
enregistrer_scores(scores)

# On affiche les scores de l'utilisateur
print("Vous finissez la partie avec {0} points.".format(scores[utilisateur]))

os.system("pause")
