import random

print("Bienvenue dans le jeu 'Pierre, papier, ciseaux', vous devez devez battre l'ordinateur !")
userInput = input("Entrez pierre, papier ou ciseaux pour tentez de battre la machine :\n")
userInput = userInput.lower()
userInput.replace(" ","")

elements = ["pierre","papier","ciseaux"]

while userInput not in elements:
    userInput = input("Erreur : entrez correctement le mot papier, feuille ou ciseaux :\n")    

randNumber = random.randint(0,2)
randElement = elements[randNumber]

while randElement == userInput:
    print("Vous avez choisi : "+userInput+"\n")
    print("L'ordinateur à choisi : "+randElement+"\n")
    print("EGALITE !\n")
    userInput = input("Entrez pierre, papier ou ciseaux pour tentez de battre la machine :\n")
    userInput = userInput.lower()
    userInput.replace(" ","")
    while userInput not in elements:
        userInput = input("Erreur : entrez correctement le mot papier, feuille ou ciseaux :\n")
    randNumber = random.randint(0,2)
    randElement = elements[randNumber]

if randElement == "pierre" and userInput == "papier":
    print("Vous avez choisi : "+userInput+"\n")
    print("L'ordinateur à choisi : "+randElement+"\n")
    print("vous avez gagné !")
elif randElement == "pierre" and userInput == "ciseaux":
    print("Vous avez choisi : "+userInput+"\n")
    print("L'ordinateur à choisi : "+randElement+"\n")
    print("vous avez perdu !")
elif randElement == "papier" and userInput == "ciseaux":
    print("Vous avez choisi : "+userInput+"\n")
    print("L'ordinateur à choisi : "+randElement+"\n")
    print("vous avez gagné !")
elif randElement == "papier" and userInput == "pierre":
    print("Vous avez choisi : "+userInput+"\n")
    print("L'ordinateur à choisi : "+randElement+"\n")
    print("vous avez perdu !")
elif randElement == "ciseaux" and userInput == "pierre":
    print("Vous avez choisi : "+userInput+"\n")
    print("L'ordinateur à choisi : "+randElement+"\n")
    print("vous avez gagné !")
elif randElement == "ciseaux" and userInput == "papier":
    print("Vous avez choisi : "+userInput+"\n")
    print("L'ordinateur à choisi : "+randElement+"\n")
    print("vous avez perdu !")