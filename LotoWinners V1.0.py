
#coding by : phenix 
#version Build : V1.0

import random

print("Welecome to the game LotoWinner V1.0 coding by phenix and charlie haid")
# ici se trouve le mecanisme ou le programme choisie un nombre au hasard et le stock dans une variable .
n = random.randint(0,20)
appreciation = "?"
while True:
    var = input("Entrez un nombre , valent de 1 a 20 et essaye de trouver celui que j'ai selectioner ;) : ")
    var = int(var)
    if var < n :
        appreciation = "ton nombre et trop bas , ressayer"
        print(var, appreciation)

    else :
        appreciation = "ton nombre et trop haut , ressayer"
        print(var, appreciation)
    if var == n:
        appreciation = "bravo BG tu a trouver le chiffre que j'ai choisi ! , Merci d'avoir jouer a se jeux  , n'eshite pas a nous envoyer ton avis sur notre ghithub ;)"
        print(var, appreciation)
        break

#Bien sur se n'est pas un jeux de fou , c'est un petit script qui devine un nombre et ou vous dever le retrouver mais sacher que j'ai eux c'ette idée de coder se script, apres avoir vu une perssone en ville 
#qui deviner un nombre , et ou c'etais compliquer de trouver le nombre que il a choisit , et je remercie charlie de m'avoir donnée c'ette idée .
