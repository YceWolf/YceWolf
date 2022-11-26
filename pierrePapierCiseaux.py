import random

# pi g ci / pi p pa / pi = pi
# pa g pi / pa p ci / pa = pa
# ci g pa / ci p oi / ci = ci

actionPlayerChoose = ["pierre", "papier", "ciseaux"]

iaActionSet = random.randint(1, 3)
iaActionSet = (iaActionSet - 1)
iaAction = actionPlayerChoose[iaActionSet]

iaNbLife = 3
nbLife = 3

print("Made by YceWolf")
print("Bon jeu !")

currentGame = True
winCondition = False
loseCondition = False
choose = "Vide"

def satenWill():

    satanHell = True

    print("Tu es bloqué ici")
    print("TU ne peux rien faire")
    print("appart,")
    input("appuie sur Exe")

    while(satanHell == True):
        print("666")

while(currentGame == True):

    iaActionSet = random.randint(1, 3)
    iaActionSet = (iaActionSet - 1)
    iaAction = actionPlayerChoose[iaActionSet]

    winCondition = False
    loseCondition = False
    choose = "Vide"

    print("Choisit entre :")
    print("0 = pierre")
    print("1 = papier")
    print("2 = ciseaux")

    actionPlayer = int(input(":"))

#pierre
    if((actionPlayer == 0) and (iaActionSet == 2)):
        print("Tu gagne !")
        print("-1 vie pour l'IA")
        iaNbLife = iaNbLife - 1
        print("Tes vie : {}".format(nbLife))
        print("Vie IA : {}".format(iaNbLife))
        input("Appuyer sur Exe")

    if((actionPlayer == 0) and (iaActionSet == 1)):
        print("Tu perd !")
        print("-1 vie pour toi")
        nbLife = nbLife - 1
        print("Tes vie : {}".format(nbLife))
        print("Vie IA : {}".format(iaNbLife))
        input("Appuyer sur Exe")

    if((actionPlayer == 0) and (iaActionSet == 0)):
        print("Egaliter !")
        print("Tes vie : {}".format(nbLife))
        print("Vie IA : {}".format(iaNbLife))
        input("Appuyer sur Exe")

#papier
    if((actionPlayer == 1) and (iaActionSet == 0)):
        print("Tu gagne !")
        print("-1 vie pour l'IA")
        iaNbLife = iaNbLife - 1
        print("Tes vie : {}".format(nbLife))
        print("Vie IA : {}".format(iaNbLife))
        input("Appuyer sur Exe")

    if((actionPlayer == 1) and (iaActionSet == 2)):
        print("Tu perd !")
        print("-1 vie pour toi")
        nbLife = nbLife - 1
        print("Tes vie : {}".format(nbLife))
        print("Vie IA : {}".format(iaNbLife))
        input("Appuyer sur Exe")

    if((actionPlayer == 1) and (iaActionSet == 1)):
        print("Egaliter !")
        print("Tes vie : {}".format(nbLife))
        print("Vie IA : {}".format(iaNbLife))
        input("Appuyer sur Exe")

#ciseaux
    if((actionPlayer == 2) and (iaActionSet == 1)):
        print("Tu gagne !")
        print("-1 vie pour l'IA")
        iaNbLife = iaNbLife - 1
        print("Tes vie : {}".format(nbLife))
        print("Vie IA : {}".format(iaNbLife))
        input("Appuyer sur Exe")

    if((actionPlayer == 2) and (iaActionSet == 0)):
        print("Tu perd !")
        print("-1 vie pour toi")
        nbLife = nbLife - 1
        print("Tes vie : {}".format(nbLife))
        print("Vie IA : {}".format(iaNbLife))
        input("Appuyer sur Exe")

    if((actionPlayer == 2) and (iaActionSet == 2)):
        print("Egaliter !")
        print("Tes vie : {}".format(nbLife))
        print("Vie IA : {}".format(iaNbLife))
        input("Appuyer sur Exe")

    if(actionPlayer == 4):
        print("Donnut skip !")
        iaNbLife = 0
        nbLife = 3
        print("Vos vie: {}, Vie IA: {}".format(nbLife, iaNbLife))

    if(actionPlayer == 666):
        print("Le diable est la !!")
        satenWill()

    if(iaNbLife == 0):
        print("You Win !")
        winCondition = True

    if(nbLife == 0):
        print("You lose !")
        loseCondition = True

    if(winCondition == True or loseCondition == True):
        print("Replay : y/n")
        choose = input(":")

    if(choose == "y"):
        print("Good luck")
        iaNbLife = 3
        nbLife = 3

    if(choose == "n"):
        print("Au revoir !")
        currentGame = False