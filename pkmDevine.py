pkmTypeFR = ["acier", "combat", "dragon", "eau", "electick", "fee", "feu", "glace", "oiseau",
 "insecte", "normal", "plante", "poison", "psy", "roche", "sol", "spectre", "tenebres", "vol"]

pkmGen = ["gen1", "gen2", "gen2", "gen3", "gen4", "gen5", "gen6", "gen7", "gen8", "gen9"]

def pkmFindFR():

    print("Made by YceWolf")

    print("Entrer pkm name")
    print("ex : e-v-o-l-i-e")
    pkmNameFindFR = input(":")

    if(pkmNameFindFR == "test"):
        pkmNameFindFR = ["e", "f", "f", "l", "e", "c", "h", "e"]
        pkmTypeFindFR = ["plante", "vol"]
        pkmEvoFindFR = 1
        pkmSousEvoFindFR = 1
        pkmGenFindFR = "gen7"
        pkmMapFindFR = "non"
        pkmNameFindFRResult = "effleche"

        pkmFindListFR = [pkmNameFindFR, pkmTypeFindFR, pkmEvoFindFR, pkmSousEvoFindFR, pkmGenFindFR, pkmMapFindFR, pkmNameFindFRResult]

        return pkmFindListFR

    pkmReplaceLetter = "-"
    pkmNameFindFRResult = "YceWolf"

    for pkmLetterFRFindName in range(len(pkmReplaceLetter)):
        pkmNameFindFRResult = pkmNameFindFR.replace(pkmReplaceLetter[pkmLetterFRFindName],"")
        print(pkmNameFindFRResult)

    pkmNameFindFR = pkmNameFindFR.split('-')

    print("Entrer pkm type")
    print("ex : eau-poison")
    pkmTypeFindFR = input(":")
    pkmTypeFindFR = pkmTypeFindFR.split('-')

    print("Entrer pkm nb évo")
    print("ex : 1")
    pkmEvoFindFR = int(input(":"))

    print("Entrer pkm nb sous-évo")
    print("ex : 0")
    pkmSousEvoFindFR = int(input(":"))

    print("Entrer pkm gen")
    print("ex : gen1")
    pkmGenFindFR = input(":")

    print("Présent sur la map")
    print("PS:Comme Dialga en gen4")
    print("ex : oui/non")
    pkmMapFindFR = input(":")

    pkmFindListFR = [pkmNameFindFR, pkmTypeFindFR, pkmEvoFindFR, pkmSousEvoFindFR, pkmGenFindFR, pkmMapFindFR, pkmNameFindFRResult]

    return pkmFindListFR

gameLaunch = True

while(gameLaunch == True):

    youWin = False
    currentGame = True

    pkmFindListFinalFR = pkmFindFR()
    pkmFindNameFinalFR = pkmFindListFinalFR[0]
    pkmFindTypeFinalFR = pkmFindListFinalFR[1]
    pkmFindEvoFinalFR = pkmFindListFinalFR[2]
    pkmFindSousEvoFinalFR = pkmFindListFinalFR[3]
    pkmFindGenFinalFR = pkmFindListFinalFR[4]
    pkmFindMapFinalFR = pkmFindListFinalFR[5]
    pkmResultFR = pkmFindListFinalFR[6]

    while(currentGame == True):

        print("Ne ragarde pas !")
        print("Ne ragarde pas !")
        print("Ne ragarde pas !")
        print("Ne ragarde pas !")
        print("Ne ragarde pas !")

        print("q1 = name question")        
        print("q2 = type question")
        print("q3 = évo question")
        print("q4 = gen question")
        print("q5 = map question")
        print("r = donner un nom de pkm")

        answer = input(":")

        if(answer == "q1"):
            print("1 = 1er lettre pkm.")
            print("2 = Dernier lettre pkm.")
            qNameFR = input(":")

            if(qNameFR == "1"):
                print(pkmFindNameFinalFR[0])
                input("Appuyez sur Exe")

            if(qNameFR == "2"):
                lenPkmFindNameFinalFR = len(pkmFindNameFinalFR)
                lenPkmFindNameFinalFR =- 1
                print(pkmFindNameFinalFR[lenPkmFindNameFinalFR])
                input("Appuyez sur Exe")


        if(answer == "q2"):
            print("3 = 1 ou 2 type ?")
            print("4 = Est-t'il type .... ?")
            print("5 = Quel(s) type(s) ?")
            qTypeFR = input(":")

            if(qTypeFR == "3"):
                lenpkmFindTypeFinalFR = len(pkmFindTypeFinalFR)
                print(lenpkmFindTypeFinalFR)
                input("Appuyez sur Exe")

            if(qTypeFR == "4"):
                pkmTypeLen = len(pkmFindTypeFinalFR)
                pkmTypeLen =- 1
                print("Donner un type")
                print("ex : poison")
                questionTypeFR = input(":")

                for qPkmType in pkmTypeFR:
                    if(qPkmType == questionTypeFR and (pkmFindTypeFinalFR[0] == questionTypeFR or pkmFindTypeFinalFR[pkmTypeLen] == questionTypeFR)):
                        print("Il possède ce type.")
                        input("Appuyez sur Exe")
                        break
                    elif(qPkmType == questionTypeFR and (questionTypeFR != pkmFindTypeFinalFR[0] or pkmFindTypeFinalFR[pkmTypeLen])):
                        print("Il ne possède pas ce type.")
                        input("Appuyez sur Exe")

            if(qTypeFR == "5"):
                print(pkmFindTypeFinalFR)
                input("Appuyez sur Exe")

        if(answer == "q3"):
            print("6 = A-t'il de évo ?")
            print("7 = Combien a t'il d'évo ?")
            print("8 = A-t'il de sous-évo ?")
            print("9 = Combien a t'il de sous-évo ?")
            qEvoFR = input(":")

            if(qEvoFR == "6"):
                if(pkmFindEvoFinalFR == 0):
                    print("Ne possède pas d'évo")
                    input("Appuyez sur Exe")

                else:
                    print("Possède une/des évo")
                    input("Appuyez sur Exe")

            if(qEvoFR == "7"):
                if(pkmFindEvoFinalFR != 0):
                    print("Possède {} évo".format(pkmFindEvoFinalFR))
                    input("Appuyez sur Exe")
                else:
                    print("Ne possède pas d'évo !")
                    input("Appuyez sur Exe")

            if(qEvoFR == "8"):
                if(pkmFindSousEvoFinalFR == 0):
                    print("Ne possède pas de sous évo")
                    input("Appuyez sur Exe")

                else:
                    print("Possède une/des sous évo")
                    input("Appuyez sur Exe")

            if(qEvoFR == "9"):
                if(pkmFindSousEvoFinalFR != 0):
                    print("Possède {} sous évo".format(pkmFindSousEvoFinalFR))
                    input("Appuyez sur Exe")
                else:
                    print("Ne possède pas de sous évo !")
                    input("Appuyez sur Exe")


        if(answer == "q4"):
            print("10 = Est-il de la gen. ?")
            print("11 = De Quel gen vient-il ?")
            qGenFR = input(":")
        
            if(qGenFR == "10"):
                print("Ecrit une gen.")
                print("ex : gen1")
                questionGenFR = input(":")
                for gen in pkmGen:
                    if(gen == questionGenFR and pkmFindGenFinalFR == questionGenFR):
                        print("Vient bien de la {}".format(pkmFindGenFinalFR))
                        input("Appuyez sur Exe")
                        break
                    elif(gen == questionGenFR and questionGenFR != pkmFindGenFinalFR):
                        print("Ne vient pas de la {}".format(questionGenFR))
                        input("Appuyez sur Exe")

            if(qGenFR == "11"):
                print("Vient de la {}".format(pkmFindGenFinalFR))
                input("Appuyez sur Exe")
                    
        if(answer == "q5"):
            print("12 = Est-il présent sur la map ?")
            print("PS : Comme Palkia en gen4")
            qMapFR = input(":")

            if(qMapFR == "12"):
                print("Présent sur la map")
                input("Appuyez sur Exe")
            else:
                print("Présent sur la map")
                input("Appuyez sur Exe")

        if(answer == "r"):
            print("Donner un nom de pkm.")
            print("ex : effleche")
            resultFR = input(":")

            if(resultFR == pkmResultFR):
                print("Tu as gagné !")
                print("Le pokémon est {}".format(pkmResultFR))
                youWin = True
                input("Appuyez sur Exe")
        
            elif(resultFR != pkmResultFR):
                print("Tu n'as pas bon")
                input("Appuyez sur Exe")

        if(youWin == True):
            replay = input("Rejouer y/n :")

            if(replay == "y"):
                print("Bonne chance et bon jeu !")
                input("Appuyez sur Exe")
        
            if(replay == "n"):
                print("Au revoir !")
                gameLaunch = False
                currentGame = False
