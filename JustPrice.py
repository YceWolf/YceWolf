import random

startGame = "True"

while(startGame == "True"):

    playerNb = input("P1 ou P2:")
    nbLife = input("Set nb life:")

    nbLifeNb = int(nbLife)

    winCondition = "False"
    lostCondition = int(0)
    restartGame = "False"
    gameLaunchP1 = True
    gameLaunchP2 = True


    if(playerNb == "P1"):

        nb = random.randint(1, 1000)
        print("Good Luck")

        while(gameLaunchP1 == True):

            nbChoice = input("Give a nb:")
            nbChoice = int(nbChoice)

            if(nbChoice > nb):
                print("Less")
                nbLifeNb = (nbLifeNb - 1)
                print("nb of life:", nbLifeNb)

            elif(nbChoice < nb):
                print("More")
                nbLifeNb = (nbLifeNb - 1)
                print("nb of life:", nbLifeNb)

            elif(nbChoice == nb):
                print("You win !")
                winCondition = "True"
                gameLaunchP1 = False

            if(nbLifeNb == lostCondition):
                print("You lose")
                print("Nb was:", nb)
                restartGame = "True"
                gameLaunchP1 = False


    if(playerNb == "P2"):

        nbFind = input("Set Nb Find:")
        nbFind = int(nbFind)

        print("Don't look !")
        print("Don't look !")
        print("Don't look !")
        print("Don't look !")
        print("Don't look !")
        print("Don't look !")
        print("Don't look !")
        print("Don't look !")

        while(gameLaunchP2 == True):

            nbChoice = input("Give a nb:")
            nbChoice = int(nbChoice)

            if(nbChoice > nbFind):
                print("Less")
                nbLifeNb = (nbLifeNb - 1)
                print("nb of life:", nbLifeNb)

            elif(nbChoice < nbFind):
                print("More")
                nbLifeNb = (nbLifeNb - 1)
                print("nb of life:", nbLifeNb)

            elif(nbChoice == nbFind):
                print("You win !")
                winCondition = "True"
                gameLaunchP2 = False

            if(nbLifeNb == lostCondition):
                print("You lose")
                print("Nb was:", nbFind)
                restartGame = "True"
                gameLaunchP2 = False


    choice = input("Replay Y/N:")
    
    if(choice == "Y"):
        print("Good Game")
        restartGame = "False"

    if(choice == "N"):
        startGame = "False"
        